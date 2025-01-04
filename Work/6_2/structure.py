# structure.py

# exercise 6.1

import sys


class Structure:
    _fields = ()

    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop("self")
        for name, value in locs.items():
            setattr(self, name, value)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})"

    def __setattr__(self, name, value):
        if name not in self._fields and name[0] != "_":
            raise AttributeError(f"No attribute {name}")
        else:
            super().__setattr__(name, value)
