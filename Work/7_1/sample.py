# sample.py

# exercise 7.1

from validate import validated, Integer
from logcall import logged


@validated
def add(x: Integer, y: Integer) -> Integer:
    return x + y


@logged
def sub(x, y):
    return x - y


@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x**y
