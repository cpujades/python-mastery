# reader.py

# exercise 2.6

import csv

import _collections_abc as collections
from abc import ABC, abstractmethod


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


class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass


class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row)}


class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)


def read_csv_as_dicts(filename, types):
    parser = DictCSVParser(types)
    return parser.parse(filename)


def read_csv_as_instances(filename, cls):
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)
