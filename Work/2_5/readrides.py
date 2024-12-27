# readrides.py

# exercise 2.5


import csv
import _collections_abc as collections
from typing import overload


class RideData(collections.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            data = RideData()
            data.routes = self.routes[idx]
            data.dates = self.dates[idx]
            data.daytypes = self.daytypes[idx]
            data.numrides = self.numrides[idx]
            return data
        return {
            "route": self.routes[idx],
            "date": self.dates[idx],
            "daytype": self.daytypes[idx],
            "rides": self.numrides[idx],
        }

    def append(self, d):
        self.routes.append(d["route"])
        self.dates.append(d["date"])
        self.daytypes.append(d["daytype"])
        self.numrides.append(d["rides"])


def read_rides_as_tuples(filename):
    """
    Read the bus ride data as a list of tuples
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_dicts(filename):
    """
    Read the bus ride data as a list of dictionaries
    """
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = {
                "route": route,
                "date": date,
                "daytype": daytype,
                "rides": rides,
            }
            records.append(record)
    return records


class Row:
    __slots__ = ["route", "date", "daytype", "rides"]

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_instances(filename):
    """
    Read the bus ride data as a list of instances
    """
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = Row(route, date, daytype, rides)
            records.append(record)
    return records


def read_rides_as_columns(filename):
    """
    Read the bus ride data as a list of columns
    """
    routes = []
    dates = []
    daytypes = []
    numrides = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)  # Skip headers
        for row in rows:
            routes.append(row[0])
            dates.append(row[1])
            daytypes.append(row[2])
            numrides.append(int(row[3]))
    return dict(route=routes, date=dates, daytype=daytypes, rides=numrides)


if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    rows = read_rides_as_dicts("../Data/ctabus.csv")
    print("Memory Use: Current %d, Peak %d" % tracemalloc.get_traced_memory())
