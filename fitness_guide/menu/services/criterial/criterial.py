class Criterial2:
    """
    Модуль решения задачи многокритериальной оптимизации.
    Задача: Требуется из списка шаблонов меню выбрать, используя параметры клиента, оптимальныt варианты шаблонов меню.

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
        self.menu_list = {}

    def set_menu_list(self, datad):
        self.menu_list = datad

    def pareto(self, restricted_prod: list, loved_prod: list, type="health", epd=3, ned=1):
        """Формирует Парето-оптимальный список шаблонов меню.
        Критерии:
        1) разница между фактическим и желаемым количеством приемов пищи (негативный) (epd)
        2) разница между фактическим и желаемым количеством разгрузочных дней (негативный) (ned)
        3) любимые продукты: число совпадений из loved_prod и general->all_products (позитивный) (love)

        Ограничения:
        1) тип диеты (general->type)
        2) аллергии (продукты из restricted_prod не содержатся в general->all_products)
        """
        pareto_list = self.menu_list.copy()
        i = 0
        while i < len(pareto_list):
            j = i + 1
            c_epd = abs(pareto_list[i]['general']['eats_per_day'] - epd)
            c_ned = abs(pareto_list[i]['general']['no_eats_day'] - ned)
            c_love = len(set(pareto_list[i]['general']['all_products']) & set(loved_prod))
            pareto_list[i]['criterias'] = {
                'epd': c_epd,
                'ned': c_ned,
                'love': c_love
            }
            if (  # Ограничения
                    (len(set(pareto_list[i]['general']['all_products']) & set(restricted_prod)) != 0) or
                    (pareto_list[i]['general']['type'] != type)
            ):
                pareto_list.pop(i)
                continue
            while j < len(pareto_list):
                if (
                    # Критерии
                    (
                        (c_epd > abs(pareto_list[j]['general']['eats_per_day'] - epd)) and
                        (c_ned > abs(pareto_list[j]['general']['no_eats_day'] - ned)) and
                        (c_love < len(set(pareto_list[j]['general']['all_products']) & set(loved_prod)))
                    )
                ):
                    pareto_list.pop(i)
                    i -= 1
                    break
                j += 1
            i += 1
        return pareto_list

    def optimization(self, pareto_list: list, weight=[1 / 3, 1 / 3, 1 / 3]):
        """ Построение обобщенного критерия """
        general_criteria = [0 for _ in pareto_list]
        for index, menu in enumerate(pareto_list):
            general_criteria[index] = ( menu['criterias']['epd'] * weight[0] +
                                        menu['criterias']['ned'] * weight[1] +
                                        menu['criterias']['love'] * weight[2])
        return pareto_list[general_criteria.index(max(general_criteria))]
