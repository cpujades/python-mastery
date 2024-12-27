# reader.py

# exercise 2.6

import csv

import _collections_abc as collections


def read_csv_as_dicts(filename, types):
    records = []
    with open(filename, "r") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records


class DataCollection(collections.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, idx):
        if isinstance(idx, slice):
            data = DataCollection()
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


def read_csv_as_columns(filename, types):
    records = DataCollection()
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {name: func(val) for name, func, val in zip(headers, types, row)}
            records.append(record)
    return records
