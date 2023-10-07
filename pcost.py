def portfolio_cost(filename):
    total_cost = 0.0
    with open(f'Data/{filename}', 'r') as f:
        for line in f:
            contents = line.split()
            try:
                shares = int(contents[1])
                price = float(contents[2])
            except ValueError as e:
                print(f"Couldn't parse: {line}Reason: {e}")
            total_cost = total_cost + (shares * price)
    return total_cost


portfolio_cost('portfolio.dat')
