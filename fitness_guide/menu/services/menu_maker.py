import os

import numpy as np
from random import randrange

from .criterial.criterial import Criterial2
from .regression.Regression import LinearRegression
from ..models import Day, DaysOfMenu, DaysOfMenu, Dish, DishesOfMeal, Ingredient, Meal, MealsOfDay, Menu, Product, Template


class Menumaker2:
    def __init__(self,
                 caloria_dump: str = "../data/regression_caloria_dump.np",
                 amino_dump: str = "../data/regression_amino_dump.np") -> None:

        path_for_caloria_dump = os.path.join(
                                    os.path.join(
                                        os.path.join(
                                            os.path.join(
                                                os.getcwd(), 'menu'),
                                            'services'),
                                        'data'),
                                    'regression_caloria_dump.np')

        path_for_amino_dump = os.path.join(
                                    os.path.join(
                                        os.path.join(
                                            os.path.join(
                                                os.getcwd(), 'menu'),
                                            'services'),
                                        'data'),
                                    'regression_amino_dump.np')

        self.criterial = Criterial2()

        self.caloria_regression = LinearRegression()
        self.caloria_regression.load(path_for_caloria_dump)

        self.amino_regression = LinearRegression()
        self.amino_regression.load(path_for_amino_dump)

    def make_menu_list(self, *args, **kwargs):
        menu_list = []
        for template in list(Template.objects.all()):
            menu = template.menu.id
            # чтобы доставать сразу несколько, надо для сгенерированного листа выполнить функцию преобразования через map в новый лист
            # где к каждому элементу старого массива будем применять функцию типа .day.id / .product.name
            day = list(map(lambda x: x.day.id, list(DaysOfMenu.objects.filter(menu=menu))))
            meal = list(map(lambda x: x.meal.id, list(MealsOfDay.objects.filter(day__in=day))))
            dish = list(map(lambda x: x.dish.id, list(DishesOfMeal.objects.filter(meal__in=meal))))
            product = set(map(lambda x: x.product.name, list(Ingredient.objects.filter(dish__in=dish))))
            menu_list.append(
                {
                    "id": template.id,
                    "general": {
                        "eats_per_day": randrange(9),
                        "type": template.type_diet,
                        "no_eats_day": randrange(9),
                        "all_products": product
                    },
                    "menu": {
                      "Monday": {
                        "calories": 3553,
                        "proteins": 193,
                        "fats": 128,
                        "carbohydrates": 482,
                        "weight": 1389,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Греческий йогурт",
                              "Малина",
                              "Мюсли (ванильные, миндальные, или без наполнителей)",
                              "Яйца"
                            ],
                            "recipe": "Яйца сварить и нарезать. Всё перемешать"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Макароны",
                              "Морковь",
                              "Лук"
                            ],
                            "recipe": "Паста с курицей. Сварить макароны, пожарить курицу с морковкой и луком"
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Банан",
                              "Молоко",
                              "Сдобная булочка"
                            ],
                            "recipe": "Смузи с бананом и молоком. Вприкуску булочка"
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Рыба",
                              "Гречка",
                              "Капуста",
                              "Морковь",
                              "Укроп",
                              "Петрушка"
                            ],
                            "recipe": "Сварить гречку. Запечь рыбу. Сделать салат из капусты, морковки и зелени, заправленный уксусом."
                          }
                        }
                      },
                      "Tuesday": {
                        "calories": 3766,
                        "proteins": 201,
                        "fats": 103,
                        "carbohydrates": 528,
                        "weight": 1206,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Овсянка",
                              "Орехи",
                              "Молоко",
                              "Яблоки"
                            ],
                            "recipe": "Сварить овсянку с молоком. Заправить орехами и порезанным на кусочки яблоком"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Гречка",
                              "Морковь",
                              "Лук"
                            ],
                            "recipe": "Сварить гречку, пожарить курицу с морковкой и луком"
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Банан",
                              "Кефир",
                              "Сдобная булочка"
                            ],
                            "recipe": "Есть, закусывая одно другим"
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Рыба",
                              "Рис",
                              "Капуста",
                              "Морковь",
                              "Укроп",
                              "Петрушка"
                            ],
                            "recipe": "Сварить рис. Запечь рыбу. Сделать салат из капусты, морковки и зелени, заправленный уксусом."
                          }
                        }
                      },
                      "Wednesday": {
                        "calories": 3445,
                        "proteins": 162,
                        "fats": 108,
                        "carbohydrates": 407,
                        "weight": 955,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Пшенная крупа",
                              "Орехи",
                              "Молоко",
                              "Яблоки"
                            ],
                            "recipe": "Сварить пшено с молоком. Заправить орехами и порезанным на кусочки яблоком"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Свиное филе",
                              "Гречка",
                              "Морковь",
                              "Лук"
                            ],
                            "recipe": "Сварить гречку, пожарить свинину с морковкой и луком"
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Чернослив",
                              "Курага",
                              "Мороженое",
                              "Какао-порошок",
                              "Батон"
                            ],
                            "recipe": "Смешать мороженое с черносливом и курагой. Посыпать сверху какао. Вприкуску батон"
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Рис",
                              "Листья салата",
                              "Перец",
                              "Сливочное масло",
                              "Хлеб чёрный"
                            ],
                            "recipe": "Сварить рис. Запечь куриную грудку. Сделать бутерброды из сливочного масла, перца и листьев салата на чёрном хлебе"
                          }
                        }
                      },
                      "Thursday": {
                        "calories": 3322,
                        "proteins": 166,
                        "fats": 117,
                        "carbohydrates": 415,
                        "weight": 1008,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Пшенная крупа",
                              "Орехи",
                              "Молоко",
                              "Яблоки"
                            ],
                            "recipe": "Сварить пшено с молоком. Заправить орехами и порезанным на кусочки яблоком"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Гречка",
                              "Морковь",
                              "Лук"
                            ],
                            "recipe": "Сварить гречку, пожарить куриную грудку с морковкой и луком"
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Чернослив",
                              "Курага",
                              "Мороженое",
                              "Какао-порошок",
                              "Батон"
                            ],
                            "recipe": "Смешать мороженое с черносливом и курагой. Посыпать сверху какао. Вприкуску батон"
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Рис",
                              "Листья салата",
                              "Перец",
                              "Сливочное масло",
                              "Хлеб чёрный"
                            ],
                            "recipe": "Сварить рис. Запечь куриную грудку. Сделать бутерброды из сливочного масла, перца и листьев салата на чёрном хлебе"
                          }
                        }
                      },
                      "Friday": {
                        "calories": 3413,
                        "proteins": 170,
                        "fats": 121,
                        "carbohydrates": 405,
                        "weight": 990,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Овсянка",
                              "Орехи",
                              "Молоко",
                              "Яблоки"
                            ],
                            "recipe": "Сварить овсянку с молоком. Заправить орехами и порезанным на кусочки яблоком"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Гречка",
                              "Морковь",
                              "Лук"
                            ],
                            "recipe": "Сварить гречку, пожарить куриную грудку с морковкой и луком"
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Чернослив",
                              "Курага",
                              "Мороженое",
                              "Какао-порошок",
                              "Батон"
                            ],
                            "recipe": "Смешать мороженое с черносливом и курагой. Посыпать сверху какао. Вприкуску батон"
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Рис",
                              "Листья салата",
                              "Перец",
                              "Сливочное масло",
                              "Хлеб чёрный"
                            ],
                            "recipe": "Сварить рис. Запечь куриную грудку. Сделать бутерброды из сливочного масла, перца и листьев салата на чёрном хлебе"
                          }
                        }
                      },
                      "Saturday": {
                        "calories": 3707,
                        "proteins": 167,
                        "fats": 124,
                        "carbohydrates": 482,
                        "weight": 1201,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Греческий йогурт",
                              "Малина",
                              "Изюм",
                              "Гранола"
                            ],
                            "recipe": "Всё перемешать"
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Куриная грудка",
                              "Гречка",
                              "Морковь",
                              "Лук",
                              "Томатная паста"
                            ],
                            "recipe": "Сварить гречку, пожарить курицу с морковкой и луком, заправить томатной пастой."
                          }
                        },
                        "after workout": {
                          "eat": {
                            "products": [
                              "Банан",
                              "Молоко",
                              "Орехи",
                              "Творог"
                            ],
                            "recipe": "Всё перемешать."
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Рыба",
                              "Гречка",
                              "Капуста",
                              "Морковь",
                              "Укроп",
                              "Петрушка"
                            ],
                            "recipe": "Сварить гречку. Запечь рыбу. Сделать салат из капусты, морковки и зелени, заправленный уксусом."
                          }
                        }
                      },
                      "Sunday": {
                        "calories": 3116,
                        "proteins": 163,
                        "fats": 122,
                        "carbohydrates": 426,
                        "weight": 845,
                        "breakfast": {
                          "eat": {
                            "products": [
                              "Овсянка",
                              "Молоко"
                            ],
                            "recipe": "Сварить овсянку на молоке."
                          }
                        },
                        "dinner": {
                          "eat": {
                            "products": [
                              "Картофель",
                              "Гречка",
                              "Морковь",
                              "Лук",
                              "Чеснок"
                            ],
                            "recipe": "Гречневый суп."
                          }
                        },
                        "supper": {
                          "eat": {
                            "products": [
                              "Капуста цветная",
                              "Брокколи",
                              "Сливочное масло",
                              "Сыр",
                              "Мука пшеничная",
                              "Сливки"
                            ],
                            "recipe": "Запеканка из брокколи и цветной капусты."
                          }
                        }
                      }
                    }
                }
            )
        self.criterial.set_menu_list(menu_list)

    def make_menu(self, human: dict) -> dict:
        """
        :param human: dictionary with values:
            {
                "type": ['health' OR 'gain' OR 'loss'],
                "eats_per_day": how many times human wants to eat,
                "no_eats_days": how many days human wants not to eat,
                "restricted_products": LIST of STR,
                "loved_products": LIST of STR,
                "age": INT,
                "weight": INT,
                "height: INT,
                "sex": BOOL (is male?),
                "sports": INT times human doing sport a week
            }
        :return:
        """
        self.make_menu_list()

        best_menu = self.criterial.optimization(
            self.criterial.pareto(
                type=human['type'],
                epd=human['eats_per_day'],
                ned=human['no_eats_days'],
                restricted_prod=human['restricted_products'],
                loved_prod=human['loved_products']
            ),
            [1 / 3, 1 / 3, 1 / 3])

        human_calory_need = self.caloria_regression.predict(np.matrix([
            human['sex'], human['weight'], human['height'], human['age'], human['sports']
        ]))[0, 0]
        human_amino_need = self.amino_regression.predict(np.matrix([
            human['weight'], human['sports']
        ]))[0, 0]

        for day in best_menu['menu'].items():
            calory_factor = day[1]['calories'] / human_calory_need
            amino_factor = day[1]['proteins'] / human_amino_need

            if typ := human['type'] == 'gain':
                calory_factor *= 0.8
                amino_factor *= 0.5
            elif typ == 'health':
                calory_factor *= 1
            elif typ == 'loss':
                calory_factor *= 1.2
                amino_factor *= 1.2

            if human['sex']:
                calory_factor *= 0.95
            else:
                calory_factor *= 1.05

            factor = (calory_factor + amino_factor * 2) / 1.9

            best_menu['menu'][day[0]]['weight'] = round(best_menu['menu'][day[0]]['weight'] / factor)
            best_menu['menu'][day[0]]['calories'] = round(best_menu['menu'][day[0]]['calories'] / factor)
            best_menu['menu'][day[0]]['proteins'] = round(best_menu['menu'][day[0]]['proteins'] / factor)
            best_menu['menu'][day[0]]['fats'] = round(best_menu['menu'][day[0]]['proteins'] / factor)
            best_menu['menu'][day[0]]['carbohydrates'] = round(best_menu['menu'][day[0]]['proteins'] / factor)

        return best_menu
