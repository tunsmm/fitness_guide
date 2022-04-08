import json


class Criterial:
    """
    Модуль решения задачи многокритериальной оптимизации.
    Задача: Требуется из списка шаблонов меню выбрать, используя параметры клиента, несколько оптимальных вариантов шаблонов меню.

    Модуль содержит класс, реализующий следующие методы:
    Загрузка списка шаблонов меню в формате JSON (см data_specification.md) с диска
    Добавление нового шаблона
    Изменение существующего шаблона
    Сохранение шаблонов на диск
    Выбор N отпимальных вариантов по критериям клиента из зугруженного ранее списка

    Все методы следует сделать @classmethod, т.к используется паттерн "Singletone".

    В качестве параметров клиента предлагается использовать следующие величины:
    Возраст
    Рост
    Вес
    Объём физической активности
    Цель использования диеты
    Аллергические реакции
    Любимые продукты

    Любая величина, для которой существует четко определенное количество вариантов (например цель использования диеты),
    должна быть реализована в виде соответствующей сущности Python так, чтобы невозможно было подставить значение,
    не определенное в коде, без ошибки.
    """

    def __init__(self):
        """Constructor"""
        self.menu_list = []
        self.filename = ''

    def load(self, filename):
        """ Загрузка списка шаблонов меню в формате JSON с диска """
        self.filename = filename
        with open(filename, "r", encoding='utf-8') as read_file:
            self.menu_list = json.load(read_file)

    def save(self, filename=None):
        """ Сохранение шаблонов на диск """
        filename = filename if filename else self.filename
        with open(filename, "w") as write_file:
            json.dump(self.menu_list, write_file)

    def change(self, id=0, newdata={}):
        """ Изменение существующего шаблона """
        for i, v in enumerate(self.menu_list):
            if v['id'] == id:
                self.menu_list[i] = newdata

    def append(self, newdata):
        """ Добавление нового шаблона """
        if not list(filter(lambda x: x['id'] == newdata['id'], self.menu_list)):
            self.menu_list.append(newdata)

    def pareto(self, type="health", epd=3, ned=1, restricted_prod=[], loved_prod=[]):
        """Формирует Парето-оптимальный список шаблонов меню.
        Критерии:
        1) разница между фактическим и желаемым количеством приемов пищи (негативный) (epd)
        2) разница между фактическим и желаемым количеством разгрузочных дней (негативный) (ned)
        3) любимые продукты: число совпадений из loved_prod и general->all_products (позитивный) (love)

        Ограничения:
        1) тип диеты (general->type)
        2) аллергии (продукты из restricted_prod не содержатся в general->all_products)
        """
        paretolist = self.menu_list.copy()
        i = 0
        while i < len(paretolist):
            j = i+1
            c_epd = abs(paretolist[i]['general']['eats_per_day'] - epd)
            c_ned = abs(paretolist[i]['general']['no_eats_day'] - ned)
            c_love = len(set(paretolist[i]['general']['all_products']) & set(loved_prod))
            paretolist[i]['criterias'] = {
                'epd': c_epd,
                'ned': c_ned,
                'love': c_love
            }
            if (  # Ограничения
                        (len(set(paretolist[i]['general']['all_products']) & set(restricted_prod)) != 0) or
                        (paretolist[i]['general']['type'] != type)
                ):
                paretolist.pop(i)
                continue
            while j < len(paretolist):
                if (
                    # Критерии
                    (
                        (c_epd > abs(paretolist[j]['general']['eats_per_day'] - epd)) and
                        (c_ned > abs(paretolist[j]['general']['no_eats_day'] - ned)) and
                        (c_love < len(set(paretolist[j]['general']['all_products']) & set(loved_prod)))
                    )
                ):
                    paretolist.pop(i)
                    i -= 1
                    break
                j += 1
            i += 1
        return paretolist

    def optimization(self, paretolist: list, weight=[1/3, 1/3, 1/3]):
        """ Построение обобщенного критерия """
        general_criteria = [0 for _ in paretolist]
        for i, v in enumerate(paretolist):
            general_criteria[i] = (paretolist[i]['criterias']['epd'] * weight[0] +
                                   paretolist[i]['criterias']['ned'] * weight[1] +
                                   paretolist[i]['criterias']['love'] * weight[2])
        return paretolist[general_criteria.index(max(general_criteria))]
