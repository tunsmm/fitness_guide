# -*- coding: utf-8 -*-
from typing import Any, Dict, List, Tuple, Callable

import numpy as np

np.seterr(all='raise')


class Loss:
    def loss(self, w: Any, x: Any, y: Any, **kwargs: Any) -> Any:
        raise RuntimeError("loss() was not defined in class!")


class Linear(Loss):
    def loss(self, w: Any, x: Any, y: Any, **kwargs: Any) -> Any:
        raise RuntimeError("loss() was not defined in class!")


class Gradient:
    def grad(self, w: Any, x: Any, y: Any, **kwargs: Any) -> Any:
        raise RuntimeError("grad() was not defined in class!")


class LinearMSE(Linear, Gradient):
    """Mean Squared Error."""

    def loss(self,
             w: np.matrix,
             x: np.matrix,
             y: np.matrix,
             **kwargs: Any) -> float:
        """
        Loss function. Returns float value: MSE.

        Positional arguments:
            w: np.matrix. Weights of Linear regression.
            x: np.matrix. Samples.
            y: np.matrix. Real answers.
        """
        y_pred = x * w
        misses = np.array(y_pred - y)
        misses = misses**2
        loss = np.sum(misses) / len(y)
        return loss

    def grad(self,
             w: np.matrix,
             x: np.matrix,
             y: np.matrix,
             **kwargs: Any) -> np.matrix:
        """
        Gradient vector function for linear regression. Returns grad vector.

        Positional arguments:
            w: np.matrix. Weights of Linear regression.
            x: np.matrix. Samples.
            y: np.matrix. Real answers.
        """
        gradvec = []
        for j, _ in enumerate(w):
            gradcoord = np.sum([2 * x[i, j] * (x[i] * w - y[i])
                                for i in range(x.shape[0])]) / x.shape[0]
            gradvec.append(gradcoord)
        return np.matrix(gradvec)
