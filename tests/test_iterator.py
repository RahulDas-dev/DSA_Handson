import unittest
from code.iterator import DateIteraor, n_item_groupped
from datetime import datetime, timedelta


class TestNItemGroupped(unittest.TestCase):
    def test_case_1(self):
        l1 = [i for i in range(10)]
        iterator = n_item_groupped(l1, 2)
        self.assertTupleEqual(next(iterator), (0, 1))
        self.assertTupleEqual(next(iterator), (2, 3))
        self.assertTupleEqual(next(iterator), (4, 5))
        self.assertTupleEqual(next(iterator), (6, 7))
        self.assertTupleEqual(next(iterator), (8, 9))
        self.assertRaises(StopIteration, next, iterator)

    def test_case_2(self):
        iterator = n_item_groupped(range(9), 2)
        self.assertTupleEqual(next(iterator), (0, 1))
        self.assertTupleEqual(next(iterator), (2, 3))
        self.assertTupleEqual(next(iterator), (4, 5))
        self.assertTupleEqual(next(iterator), (6, 7))
        self.assertTupleEqual(next(iterator), (8, None))
        self.assertRaises(StopIteration, next, iterator)

    def test_case_3(self):
        iterator = n_item_groupped(range(10), 3)
        self.assertTupleEqual(next(iterator), (0, 1, 2))
        self.assertTupleEqual(next(iterator), (3, 4, 5))
        self.assertTupleEqual(next(iterator), (6, 7, 8))
        self.assertTupleEqual(next(iterator), (9, None, None))
        self.assertRaises(StopIteration, next, iterator)


class TestDateIterator(unittest.TestCase):
    def test_case_1(self):
        date = datetime.now()
        diterator = DateIteraor(date, 3)
        self.assertEqual(next(diterator), date - timedelta(days=1))
        self.assertEqual(next(diterator), date - timedelta(days=2))
        self.assertEqual(next(diterator), date - timedelta(days=3))
        self.assertRaises(StopIteration, next, diterator)


if __name__ == "__main__":
    unittest.main()
