# -*- coding: utf-8 -*-
from typing import Any, Tuple, Union

import numpy as np

from .Loss import LinearMSE as LG

np.seterr(all='raise')


class Optimization:
    def step(self, w: Any, x: Any, y: Any, **kwargs: Any) -> Any:
        raise RuntimeError("step() was not defined in class!")


class Linear(Optimization):
    def step(self, w: Any, x: Any, y: Any, **kwargs: Any) -> Tuple[Any, Any]:
        raise RuntimeError("step() was not defined in class!")


class Gradient(Linear):
    def __init__(self, lossObj: LG, **kwargs: Union[int, float]) -> None:
        self._random_weight = kwargs.get("random_weight", 0.001)
        self._random_grad = kwargs.get("random_grad", 0)
        self._lossObj = lossObj
        if not isinstance(lossObj, LG):
            raise TypeError("lossObj is not a Gradient loss function")

    def loss(self, w: np.matrix, x: np.matrix, y: np.matrix) -> float:
        return self._lossObj.loss(w, x, y)

    def step(self,
             w: np.matrix,
             x: np.matrix,
             y: np.matrix,
             **kwargs: Any) -> Tuple[np.matrix, float]:
        max_loss_try = kwargs.get("max_loss_try", 10)
        lr = kwargs.get("lr", 0.001)

        old_loss = self.loss(w, x, y)
        loss = old_loss + 1

        while (max_loss_try > 0) and (old_loss < loss):
            try_w = self._prep_weights(w)
            try_g = self._gradient(try_w, x, y)
            try_w = self._upd_weights(try_g, try_w, lr=lr)
            loss = self.loss(try_w, x, y)
            max_loss_try -= 1
            lr /= 2

        return try_w, lr

    def _gradient(self,
                  w: np.matrix,
                  x: np.matrix,
                  y: np.matrix) -> np.ndarray:
        g = self._lossObj.grad(w, x, y).reshape(*w.shape)
        return g + np.random.randn(*g.shape) * self._random_grad

    def _prep_weights(self, w: np.matrix) -> np.matrix:
        return w + np.random.randn(*w.shape) * self._random_weight

    def _upd_weights(self,
                     g: np.ndarray,
                     w: np.matrix,
                     lr: float) -> np.matrix:
        return w - g * lr


class SGD(Gradient):
    def __init__(self, lossObj: LG, **kwargs: Union[float, int]) -> None:
        super().__init__(lossObj, **kwargs)
        self._batch_size = int(kwargs.get("batch_size", 10))

    def step(self,
             w: np.matrix,
             x: np.matrix,
             y: np.matrix,
             **kwargs: Any) -> np.matrix:
        lr = kwargs.get("lr", 0.001)
        w = self._prep_weights(w)
        x, y = self._shuffle_xy(x, y)

        for b in range(0, x.shape[0], self._batch_size):
            x_batch = x[b:b + self._batch_size]
            y_batch = y[b:b + self._batch_size]
            g = self._gradient(w, x_batch, y_batch)
            w = self._upd_weights(g, w, lr=lr)
        return w, lr

    def _shuffle_xy(self,
                    x: np.matrix,
                    y: np.matrix) -> Tuple[np.matrix, np.matrix]:
        shuffled_x = np.empty(x.shape, dtype=x.dtype)
        shuffled_y = np.empty(y.shape, dtype=y.dtype)
        permutation = np.random.permutation(len(x))
        for old_index, new_index in enumerate(permutation):
            shuffled_x[new_index] = x[old_index]
            shuffled_y[new_index] = y[old_index]
        return shuffled_x, shuffled_y


class MomentGrad(Gradient):
    def __init__(self, lossObj: LG, **kwargs: Any) -> None:
        super().__init__(lossObj, **kwargs)
        self._prev_coef = float(kwargs.get("prev_coef", 0.5))
        print(self._prev_coef)
        self._prev_g = 0

    def _upd_weights(self,
                     g: np.ndarray,
                     w: np.matrix,
                     **kwargs: Any) -> np.matrix:
        lr = kwargs['lr']
        delta_w = lr * (self._prev_coef * self._prev_g + g)
        self._prev_g = g
        return w - delta_w
