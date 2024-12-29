# tableformat.py

# exercise 3.2


def print_table(records, attributes):
    print(" ".join(f"{attr:>10}" for attr in attributes))
    print(("-" * 10 + " ") * len(attributes))
    for row in records:
        print(" ".join(f"{getattr(row, attr):>10}" for attr in attributes))
