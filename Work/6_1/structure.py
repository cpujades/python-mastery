# structure.py

# exercise 6.1


class Structure:
    _fields = ()

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f"Expected {len(self._fields)} arguments")
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})"

    def __setattr__(self, name, value):
        if name not in self._fields and name[0] != "_":
            raise AttributeError(f"No attribute {name}")
        else:
            super().__setattr__(name, value)
