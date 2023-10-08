import csv

def read_rides_as_tuples(filename: str) -> tuple:
    """Read the bus ride data as a list of tuples

    Args:
        filename (str): Filename

    Returns:
        tuple: Records from file
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records






import tracemalloc


tracemalloc.start()



tracemalloc.get_traced_memory()
tracemalloc.clear_traces()