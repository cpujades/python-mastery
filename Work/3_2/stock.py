# stock.py

# exercise 3.1

import csv


class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

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
            s = Stock(row[0], int(row[1]), float(row[2]))
            portfolio.append(s)

    return portfolio


def print_portfolio(portfolio):
    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s}")
    print(("-" * 10 + " ") * 3)
    for s in portfolio:
        print(f"{s.name:>10s} {s.shares:>10d} {s.price:>10.2f}")


if __name__ == "__main__":
    portfolio = read_portfolio("../Data/portfolio.csv")
    print_portfolio(portfolio)
