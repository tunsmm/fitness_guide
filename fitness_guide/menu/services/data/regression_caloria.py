import numpy as np

from regression.Regression import LinearRegression
from regression.Optimization import MomentGrad
from regression.Loss import LinearMSE

if __name__ == "__main__":
    dataset = np.load('caloria_xy_matrix.np', allow_pickle=True)
    data_x = dataset[:, :-1]
    data_y = dataset[:, -1]

    regressor = LinearRegression()
    regressor.fit(data_x, data_y, MomentGrad(lossObj=LinearMSE()))

    for i in range(10):
        print(data_y[i], regressor.predict(data_x[i]))

    regressor.dump('regression_caloria_dump.np')
