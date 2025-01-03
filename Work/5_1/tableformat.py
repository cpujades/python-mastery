# tableformat.py

# exercise 3.2

from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [fmt.format(d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(" ".join(f"{h:>10s}" for h in headers))
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        rowdata = [str(d) for d in rowdata]
        print(" ".join(f"{d:>10s}" for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>", end="")
        for h in headers:
            print(f"<th>{h}</th>", end="")
        print("</tr>")

    def row(self, rowdata):
        print("<tr>", end="")
        for d in rowdata:
            print(f"<td>{d}</td>", end="")
        print("</tr>")


def create_formatter(name, column_formats=None, upper_headers=False):
    if name == "text":
        formatter_cls = TextTableFormatter()
    elif name == "csv":
        formatter_cls = CSVTableFormatter()
    elif name == "html":
        formatter_cls = HTMLTableFormatter()
    else:
        raise ValueError(f"Unknown format {name}")

    if column_formats:

        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:

        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()


def print_table(records, attributes, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError("Expected a TableFormatter")

    formatter.headings(attributes)
    for r in records:
        rowdata = [getattr(r, attr) for attr in attributes]
        formatter.row(rowdata)
