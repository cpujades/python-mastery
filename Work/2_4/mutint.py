# mutint.py

# exercise 2.4

from functools import total_ordering


@total_ordering
class MutInt:
    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"MutInt({self.value})"

    def __format__(self, format_spec):
        return format(self.value, format_spec)

    # Implementing the"+" operator
    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    # Support for the reverse operation
    __radd__ = __add__

    # Implementing the in-place update operator
    def __iadd__(self, other):
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    # Implementing the "==" operator
    def __eq__(self, other):
        if isinstance(other, MutInt):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return NotImplemented

    # Implementing the "<" operator. One operator is needed for @total_ordering decorator.
    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    # Conversion to int
    def __int__(self):
        return self.value

    # Support for indexing
    __index__ = __int__

    # Conversion to float
    def __float__(self):
        return float(self.value)
