# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Tuple, Union

import numpy as np

from .Optimization import Linear as OL

np.seterr(all='raise')


class Regression:
    def fit(self, *args: Any, **kwargs: Any) -> Any:
        raise RuntimeError("fit() was not specified!")


class LinearRegression(Regression):
    _fitted: bool
    _weights: np.matrix

    def __init__(self) -> None:
        self._fitted = False

    def dump(self, filename: str):
        self._weights.dump(filename)

    def load(self, filename: str):
        self._weights = np.load(filename, allow_pickle=True)
        self._fitted = True

    def fit(self,
            x: np.matrix,
            y: np.matrix,
            opti_obj: OL,
            **kwargs: Any) -> Dict[str, list]:
        lr = float(kwargs.get("lr", 0.001))
        loss_stop = float(kwargs.get("loss_stop", 0.01))
        delta_loss_stop = float(kwargs.get("delta_loss_stop", 0.0001))
        max_iter = int(kwargs.get("max_iter", 2000))
        hot_start = bool(kwargs.get("hot_start", False))

        fit_history: Dict[str, List[Union[int, float]]] = {
            "i": [],
            "loss": [],
            "delta_loss": [],
            "weights": [],
            "lr": []
        }

        if not isinstance(opti_obj, OL):
            raise TypeError("opti_obj is not a Linear Optimization object")

        x, y = self._perpare_xy(x, y)
        if not hot_start:
            self._weights = np.random.uniform(np.min(x), np.max(x), x.shape[1])
            self._weights = np.matrix(self._weights.reshape(x.shape[1], 1))

        loss = opti_obj.loss(self._weights, x, y)
        delta_loss = delta_loss_stop + 1
        i = 0
        try:
            for i in range(max_iter):
                if loss <= loss_stop:
                    break
                if delta_loss_stop >= delta_loss > 0:
                    break
                new_lr = self._one_train(x, y, opti_obj.step, lr=lr)
                new_loss = opti_obj.loss(self._weights, x, y)

                delta_loss = loss - new_loss
                loss = new_loss

                fit_history['i'].append(i)
                fit_history['loss'].append(loss)
                fit_history['delta_loss'].append(delta_loss)
                fit_history['weights'].append(self._weights)
                fit_history['lr'].append(new_lr)

            self._fitted = True
        except Exception as e:
            raise e
        finally:
            return fit_history

    def predict(self, x: np.matrix):
        if not self._fitted:
            raise Exception("Model is not trained! Run fit() first!")

        return x*self._weights[:-1] + self._weights[-1]

    def _one_train(self,
                   x: np.matrix,
                   y: np.matrix,
                   opti_func: '(w: Any, x: Any, y: Any, kwargs: dict[str, Any]) -> tuple[Any, float]',
                   **kwargs: float) -> float:
        self._weights, lr = opti_func(self._weights, x, y, **kwargs)
        return lr

    def _perpare_xy(self,
                    x: np.matrix,
                    y: np.matrix) -> Tuple[np.matrix, np.matrix]:
        if not (isinstance(x, np.ndarray) or isinstance(x, np.matrix)):
            raise TypeError("x is not an np.array/np.matrix type")
        if not (isinstance(y, np.ndarray) or isinstance(y, np.matrix)):
            raise TypeError("y is not an np.array/np.matrix type")

        x, y = np.matrix(x), np.matrix(y)
        x = np.hstack((x, np.ones((x.shape[0], 1))))

        try:
            if x.shape[0] != y.shape[0] or y.shape[1] != 1:
                raise ValueError(f"x{x.shape} not compatible with y{y.shape}")
        except IndexError:
            raise ValueError(f"wrong: x{x.shape}, y{y.shape}: x(m,n), y(m,1)")

        return x, y


class LinearRandom(LinearRegression):
    def fit(self,
            x: np.matrix,
            y: np.matrix,
            opti_obj: OL,
            **kwargs: Any) -> Dict[str, list]:
        x, y = self._perpare_xy(x, y)
        self._weights = np.random.uniform(np.min(x), np.max(x), x.shape[1])
        self._weights = np.matrix(self._weights.reshape(x.shape[1], 1))

        loss = opti_obj.loss(self._weights, x, y)

        fit_history = {
            "i": [1],
            "loss": [loss],
            "delta_loss": [0.0],
            "weights": [self._weights],
            "lr": [0]
        }

        return fit_history
