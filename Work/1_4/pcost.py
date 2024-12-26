# pcost.py

# exercise 1.3


def portfolio_cost(filename):
    with open(filename, "r") as f:
        total_cost = 0
        for line in f:
            stocks = line.split()
            try:
                total_cost += int(stocks[1]) * float(stocks[2])
            except ValueError as e:
                print("Couldn't parse:", line, end="")
                print("Reason:", e)

    return total_cost


print(portfolio_cost("../Data/portfolio3.dat"))
