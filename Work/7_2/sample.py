# sample.py

# exercise 7.1

from validate import validated, Integer
from logcall import logformat

logged = logformat("Calling {func.__name__}")


@logged
def add(x, y):
    "Adds two things"
    return x + y


@logged
def sub(x, y):
    return x - y


@validated
def pow(x: Integer, y: Integer) -> Integer:
    return x**y


@logformat("{func.__code__.co_filename}:{func.__name__}")
def mul(x, y):
    return x * y
