# pcost.py

# exercise 1.3

with open("../../Data/portfolio.dat", "r") as f:
    total_cost = 0
    for line in f:
        stocks = line.split()
        try:
            total_cost += int(stocks[1]) * float(stocks[2])
        except ValueError:
            print("Bad line:", line)

print("Total cost:", total_cost)
