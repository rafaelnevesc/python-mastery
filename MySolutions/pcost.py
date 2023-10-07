def portfolio_cost(filename):
    total_cost = 0.0
    with open(f'../Data/{filename}', 'r') as f:
        for line in f:
            contents = line.split()
            shares = int(contents[1])
            price = float(contents[2])
            total_cost = total_cost + (shares * price)
    return total_cost


portfolio_cost('portfolio.dat')
