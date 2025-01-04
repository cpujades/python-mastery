# teststock.py

# exercise 5.6

import unittest
import stock


class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock("GOOGL", 100, 490.10)
        self.assertEqual(s.name, "GOOGL")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.10)

    def test_create_keyword(self):
        s = stock.Stock(name="GOOGL", shares=100, price=490.10)
        self.assertEqual(s.name, "GOOGL")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.10)

    def test_cost(self):
        s = stock.Stock("GOOGL", 100, 490.10)
        self.assertEqual(s.cost, 49010.0)

    def test_sell(self):
        s = stock.Stock("GOOGL", 100, 490.10)
        s.sell(25)
        self.assertEqual(s.shares, 75)

    def test_repr(self):
        s = stock.Stock("GOOGL", 100, 490.10)
        self.assertEqual(repr(s), "Stock('GOOGL', 100, 490.1)")

    def test_eq(self):
        s1 = stock.Stock("GOOGL", 100, 490.10)
        s2 = stock.Stock("GOOGL", 100, 490.10)
        self.assertEqual(s1, s2)
        self.assertEqual(s1 == s2, True)
        self.assertTrue(s1 == s2)

    def test_from_row(self):
        s = stock.Stock.from_row(["GOOGL", "100", "490.10"])
        self.assertEqual(s.name, "GOOGL")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.10)

    def test_bad_shares(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.shares = "50"

    def test_negative_shares(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(ValueError):
            s.shares = -50

    def test_bad_price(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(TypeError):
            s.price = "201.3"

    def test_negative_price(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(ValueError):
            s.price = -201.3

    def test_no_shares(self):
        s = stock.Stock("GOOG", 100, 490.1)
        with self.assertRaises(AttributeError):
            s.share = 50


if __name__ == "__main__":
    unittest.main()
