import unittest

from language.orderedList import OrderedList


class TestOrderedList(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.testList = OrderedList()

    def test_case_1(self):
        self.testList.add(3)
        self.assertListEqual(self.testList.values, [3])
        self.testList.add(2)
        self.assertListEqual(self.testList.values, [2, 3])
        self.testList.add(4)
        self.assertListEqual(self.testList.values, [2, 3, 4])
        self.testList.add(3)
        self.assertListEqual(self.testList.values, [2, 3, 3, 4])
        self.testList.add(5)
        self.assertListEqual(self.testList.values, [2, 3, 3, 4, 5])
        self.testList.add(1)
        self.assertListEqual(self.testList.values, [1, 2, 3, 3, 4, 5])

    def test_case_2(self):
        self.testList.remove(3)
        self.assertListEqual(self.testList.values, [1, 2, 3, 4, 5])
        self.testList.remove(1)
        self.assertListEqual(self.testList.values, [2, 3, 4, 5])
        self.testList.remove(5)
        self.assertListEqual(self.testList.values, [2, 3, 4])
        self.testList.remove(3)
        self.assertListEqual(self.testList.values, [2, 4])


if __name__ == "__main__":
    unittest.main()
