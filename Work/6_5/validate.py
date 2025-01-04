# validate.py

# exercise 6.5

import inspect


class ValidatedFunction:
    def __init__(self, func):
        self.func = func
        self.signature = inspect.signature(func)
        self.annotations = dict(func.__annotations__)
        self.retcheck = self.annotations.pop("return", None)

    def __call__(self, *args, **kwargs):
        bound = self.signature.bind(*args, **kwargs)

        for name, val in self.annotations.items():
            val.check(bound.arguments[name])

        result = self.func(*args, **kwargs)

        if self.retcheck:
            self.retcheck.check(result)

        return result


if __name__ == "__main__":

    def add(x: int, y: int) -> int:
        return x + y

    add = ValidatedFunction(add)
