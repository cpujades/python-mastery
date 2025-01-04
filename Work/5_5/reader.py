# reader.py

# exercise 5.1

import csv

from typing import List, Iterable
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def convert_csv(lines, converter, has_headers=True):
    """
    Convert lines of text into a list of lists
    """
    records = []
    rows = csv.reader(lines)
    if has_headers:
        headers = next(rows)
    for i, row in enumerate(rows, start=1):
        try:
            records.append(converter(headers, row))
        except ValueError as e:
            logger.warning(f"Row {i}: Bad row: {row}")
            logger.debug(f"Row {i}: Reason: {e}")
    return records


def csv_as_dicts(lines: Iterable, types: List, has_headers: bool = True) -> List:
    """
    Convert lines of text into a list of dictionaries
    """
    records = convert_csv(
        lines,
        lambda headers, row: {
            name: func(val) for name, func, val in zip(headers, types, row)
        },
        has_headers,
    )
    return records


def csv_as_instances(lines: Iterable, cls, has_headers: bool = True) -> List:
    """
    Convert lines of text into a list of instances
    """
    records = convert_csv(lines, lambda headers, row: cls.from_row(row), has_headers)
    return records


def read_csv_as_dicts(filename: str, types: List) -> List:
    """
    Read a CSV file with type conversion into a list of dictionaries
    """
    with open(filename) as f:
        records = csv_as_dicts(f, types, has_headers=True)
    return records


def read_csv_as_instances(filename: str, cls: type) -> List:
    """
    Read a CSV file with a class into a list of instances
    """
    with open(filename) as f:
        records = csv_as_instances(f, cls, has_headers=True)
    return records
