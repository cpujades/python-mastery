# readport.py

# exercise 2.2


import csv


def read_portfolio(filename):
    """
    Reads a file and return a list of dicts
    """
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            record = {"name": row[0], "shares": int(row[1]), "price": float(row[2])}
            portfolio.append(record)
    return portfolio
