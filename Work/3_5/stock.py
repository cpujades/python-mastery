# stock.py

# exercise 3.4

import csv


class Stock:
    __slots__ = ("name", "_shares", "_price")
    _types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        row = [func(val) for func, val in zip(cls._types, row)]
        return cls(*row)

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected an {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected a {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares):
        self.shares -= shares


def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            s = Stock.from_row(row)
            portfolio.append(s)

    return portfolio


def print_portfolio(portfolio):
    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s}")
    print(("-" * 10 + " ") * 3)
    for s in portfolio:
        print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")


if __name__ == "__main__":
    import tableformat
    import reader

    # portfolio = read_portfolio("../Data/portfolio.csv")
    portfolio = reader.read_csv_as_instances("../Data/portfolio.csv", Stock)
    tableformat.print_table(portfolio, ["name", "shares", "price"])
