import numpy as np
import json

"""
Human parameters:
------------------
weight: float, kilograms
sport_a_week: do sport times a week. Unsigned int. Amount.

Functions:
-------------------
amino_function()
    calculates pure protein need for human.


"""


def dump_dataset(dataset: np.matrix, description: dict) -> None:
    np.savetxt('amino_dataset.csv', dataset, delimiter=',')

    with open('amino_description.json', 'w') as desc_file:
        json.dump(description, desc_file)

    dataset.dump('amino_xy_matrix.np')


def generate_dataset(samples: int, noise_factor: float = 1.1,
                     weights: (int, int) = (10,50),
                     sports: (int,int) = (0,5) ) -> (dict, np.matrix):

    dataset_description = {
        'matrix_cols': ['weight_X', 'sport_a_week_X', 'AMINO_Y'],
        'samples': samples,
        'noise_factor': noise_factor,
        'weights': weights,
        'sports': sports,
    }

    # matrix samples*5: columns: sex, weight, height, age, sport_a_week
    column_weight = (weights[1] - weights[0]) * np.random.random((samples, 1)) + weights[0]
    column_sport = (sports[1] - sports[0]) * np.random.random((samples, 1)) + sports[0]

    data_x = column_weight
    data_x = np.append(data_x, column_sport, axis=1)

    data_y = np.matrix([amino_function(h[0], h[1]) for h in data_x]).transpose()

    return np.append(data_x, data_y, axis=1), dataset_description


def amino_function(weight: float, sport_a_week: int) -> float:
    """
    Calculates 24hour calory need.
    Returns -1 in any error case.
    :param weight: float, kilograms
    :param sport_a_week: int, times. do sport times a week amount.
    :return:
    """

    amino = -1

    if sport_a_week <= 0:
        amino = 1.4*weight
    elif 3 >= sport_a_week >= 1:
        amino = 2.2*weight
    elif 5 >= sport_a_week > 3:
        amino = 3.4*weight
    elif 7 >= sport_a_week > 5:
        amino = 4*weight
    else:
        amino = weight

    return amino


if __name__ == "__main__":
    data, desc = generate_dataset(200)
    dump_dataset(data, desc)