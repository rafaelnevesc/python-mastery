total_cost = 0.0

with open('../Data/portfolio.dat', 'r') as f:
    for line in f:
        contents = line.split()
        shares = int(contents[1])
        price = float(contents[2])
        total_cost = total_cost + (shares * price)

print(total_cost)
