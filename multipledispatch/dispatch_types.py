# from typing import Iterator, Iterable
from collections.abc import Iterable
from numbers import Number
from datetime import datetime

from multipledispatch import dispatch
import numpy as np
import pandas as pd


@dispatch(str)
def add(a):
    print("a" + a)


# @dispatch((int, float))
@dispatch(Number)  # works also for numpy.int64, ...
def add(a):
    print(1 + a)


@dispatch(Iterable)
def add(a):
    print([add(a_) for a_ in a])


@dispatch(datetime)
def add(a):
    print("date: ", a)


add("a")
add(2)
add(2.3)
add([1, 2, 3])
add(np.array([1, 2, 3]))
add(pd.to_datetime("2031"))
