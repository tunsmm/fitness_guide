import numpy as np
import json

"""
Human parameters:
------------------
sex: male? True/False
weight: float, kilograms
height: float, santimeters
age: float, years
sport_a_week: do sport times a week. Unsigned int. Amount.

Functions:
-------------------
caloria_function()
    calculates pure calory need for human.


"""


def dump_dataset(dataset: np.matrix, description: dict) -> None:
    np.savetxt('caloria_dataset.csv', dataset, delimiter=',')

    with open('caloria_description.json', 'w') as desc_file:
        json.dump(description, desc_file)

    dataset.dump('caloria_xy_matrix.np')


def generate_dataset(samples: int, noise_factor: float = 1.1,
                     weights: (int, int) = (10,50),
                     heights: (int, int) = (160,200),
                     ages: (int, int) = (16,45),
                     sports: (int,int) = (0,5) ) -> (dict, np.matrix):

    dataset_description = {
        'matrix_cols': ['sex_X','weight_X','height_X','age_X','sport_a_week_X','CALORIA_Y'],
        'samples': samples,
        'noise_factor': noise_factor,
        'weights': weights,
        'heights': heights,
        'ages': ages,
        'sports': sports,
    }

    # matrix samples*5: columns: sex, weight, height, age, sport_a_week
    column_weight = (weights[1] - weights[0]) * np.random.random((samples, 1)) + weights[0]
    column_height = (heights[1] - heights[0]) * np.random.random((samples, 1)) + heights[0]
    column_age = (ages[1] - ages[0]) * np.random.random((samples, 1)) + ages[0]
    column_sport = (sports[1] - sports[0]) * np.random.random((samples, 1)) + sports[0]

    data_x = np.random.choice([True, False], size=(samples,1))
    data_x = np.append(data_x, column_weight, axis=1)
    data_x = np.append(data_x, column_height, axis=1)
    data_x = np.append(data_x, column_age, axis=1)
    data_x = np.append(data_x, column_sport, axis=1)

    data_y = np.matrix([caloria_function(bool(h[0]), h[1], h[2], h[3], h[4]) for h in data_x]).transpose()

    return np.append(data_x, data_y, axis=1), dataset_description



def caloria_function(is_male: bool, weight: float, height: float, age: float, sport_a_week: int) -> float:
    """
    Calculates 24hour calory need.
    Returns -1 in any error case.
    :param is_male: True/False. Does human have MALE sex?
    :param weight: float, kilograms
    :param height: float, santimeters
    :param age: float, years
    :param sport_a_week: int, times. do sport times a week amount.
    :return:
    """

    bmr = -1

    if is_male:
        bmr = 88.36 + (13.4*weight) + (4.8 * height) + (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) + (4.3 * age)

        return bmr

    if sport_a_week <= 0:
        bmr *= 1.2
    elif 3 >= sport_a_week >= 1:
        bmr *= 1.375
    elif 5 >= sport_a_week > 3:
        bmr *= 1.55
    elif 7 >= sport_a_week > 5:
        bmr *= 1.725
    else:
        bmr *= 1.9

    return bmr


if __name__ == "__main__":
    data, desc = generate_dataset(200)
    dump_dataset(data, desc)