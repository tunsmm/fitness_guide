import os

import numpy as np

from .criterial.criterial import Criterial
from .regression.Regression import LinearRegression


class Menumaker:
    def __init__(self,
                 menu_templates: str = "../data/menu_templates.json",
                 caloria_dump: str = "../data/regression_caloria_dump.np",
                 amino_dump: str = "../data/regression_amino_dump.np") -> None:

        path_for_menu_templates = os.path.join(
                                    os.path.join(
                                        os.path.join(
                                            os.path.join(
                                                os.getcwd(), 'menu'),
                                            'services'),
                                        'data'),
                                    'menu_templates.json')
        
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
        
        self.criterial = Criterial()
        self.criterial.load(path_for_menu_templates)

        self.caloria_regression = LinearRegression()
        self.caloria_regression.load(path_for_caloria_dump)

        self.amino_regression = LinearRegression()
        self.amino_regression.load(path_for_amino_dump)

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

        best_menu = self.criterial.optimization(
            self.criterial.pareto(
                type=human['type'],
                epd=human['eats_per_day'],
                ned=human['no_eats_days'],
                restricted_prod=human['restricted_products'],
                loved_prod=human['loved_products']
            ),
            [1/3, 1/3, 1/3])

        human_calory_need = self.caloria_regression.predict(np.matrix([
            human['sex'], human['weight'], human['height'], human['age'], human['sports']
        ]))[0, 0]
        human_amino_need = self.amino_regression.predict(np.matrix([
            human['weight'], human['sports']
        ]))[0, 0]

        for day in best_menu['menu'].items():
            calory_factor = day[1]['calories']/human_calory_need
            amino_factor = day[1]['proteins']/human_amino_need

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

            factor = (calory_factor + amino_factor*2)/1.9

            best_menu['menu'][day[0]]['weight'] /= factor
            best_menu['menu'][day[0]]['calories'] /= factor
            best_menu['menu'][day[0]]['proteins'] /= factor

        return best_menu
