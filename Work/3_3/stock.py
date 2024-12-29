# stock.py

# exercise 3.3

import csv


class Stock:
    types = (str, int, float)

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        row = [func(val) for func, val in zip(cls.types, row)]
        return cls(*row)

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
