import numpy as np
from typing import List, Tuple


### YOU MANY NOT ADD ANY MORE IMPORTS (you may add more typing imports)

class MinMaxScaler:
    def __init__(self):
        self.minimum = None
        self.maximum = None

    def _check_is_array(self, x: np.ndarray) -> np.ndarray:
        """
        Try to convert x to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(x, np.ndarray):
            x = np.array(x)

        assert isinstance(x, np.ndarray), "Expected the input to be a list"
        return x

    def fit(self, x: np.ndarray) -> None:
        x = self._check_is_array(x)
        self.minimum = x.min(axis=0)
        self.maximum = x.max(axis=0)

    def transform(self, x: np.ndarray) -> list:
        """
        MinMax Scale the given vector
        """
        x = self._check_is_array(x)
        diff_max_min = self.maximum - self.minimum


        return (x - self.minimum) / (self.maximum - self.minimum)

    def fit_transform(self, x: list) -> np.ndarray:
        x = self._check_is_array(x)
        self.fit(x)
        return self.transform(x)


class StandardScaler:
    def __init__(self):
        self.mean = None
        self.std = None

    def _check_is_array(self, y: np.ndarray) -> np.ndarray:
        """
        Try to convert y to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(y, np.ndarray):
            y = np.array(y)

        assert isinstance(y, np.ndarray), "Expected the input to be a list"
        return y

    def fit(self, y: np.ndarray) -> None:
        y = self._check_is_array(y)
        self.mean = y.mean(axis=0)
        self.std = y.std(axis=0)

    def transform(self, y: np.ndarray) -> list:
        y = self._check_is_array(y)
        return (y - self.mean) / (self.std)

    def fit_transform(self, y: list) -> np.ndarray:
        y = self._check_is_array(y)
        self.fit(y)
        return self.transform(y)


class LabelEncoder:
    def __init__(self):
        self.length = None

    def _check_is_array(self, y: np.ndarray) -> np.ndarray:
        """
        Try to convert y to a np.ndarray if it'a not a np.ndarray and return. If it can't be cast raise an error
        """
        if not isinstance(y, np.ndarray):
            y = np.array(y)

        assert isinstance(y, np.ndarray), "Expected the input to be a list"
        return y

    def fit(self, y: np.ndarray) -> None:
        y = self._check_is_array(y)
        self.length = len(y)

    def transform(self, y: np.ndarray) -> list:
        y = self._check_is_array(y)
        return [i for i in range(len(y))]

    def fit_transform(self, y: list) -> np.ndarray:
        y = self._check_is_array(y)
        self.fit(y)
        return self.transform(y)