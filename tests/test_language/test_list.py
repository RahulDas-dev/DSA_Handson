import unittest

from language.list import flatten_list


class TestFlattenList(unittest.TestCase):
    def test_case_1(self):
        l1 = [[1, 2, 3], [4, 5, 6]]
        iterator = flatten_list(l1)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)
        self.assertEqual(next(iterator), 5)
        self.assertEqual(next(iterator), 6)
        self.assertRaises(StopIteration, next, iterator)

    def test_case_2(self):
        l1 = [[1, 2, 3], [4, 5], 6]
        iterator = flatten_list(l1)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 2)
        self.assertEqual(next(iterator), 3)
        self.assertEqual(next(iterator), 4)
        self.assertEqual(next(iterator), 5)
        self.assertEqual(next(iterator), 6)
        self.assertRaises(StopIteration, next, iterator)


if __name__ == "__main__":
    unittest.main()
