import unittest

from linkedlist.linkedlist import LinkedList


class TestOrderedList(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.testList = LinkedList()

    def tearDown(self) -> None:
        super().tearDown()
        self.testList = None

    def test_case_1(self):
        self.assertIsNone(self.testList.head)
        self.assertEqual(str(self.testList), "NULL")
        self.testList.push(4)
        self.assertEqual(self.testList.head.data, 4)
        self.testList.push(8)
        self.assertEqual(self.testList.head.fnext.data, 8)
        self.testList.push(16)
        self.assertEqual(self.testList.head.fnext.fnext.data, 16)
        self.assertEqual(str(self.testList), "4->8->16->NULL")

    def test_case_2(self):
        self.testList.push(5)
        self.testList.push(10)
        self.testList.push(15)
        self.assertEqual(str(self.testList), "5->10->15->NULL")
        x = self.testList.pop()
        self.assertEqual(self.testList.head.fnext.data, 10)
        self.assertEqual(str(self.testList), "5->10->NULL")
        self.assertEqual(x.data, 15)
        x = self.testList.pop()
        self.assertEqual(self.testList.head.data, 5)
        self.assertEqual(str(self.testList), "5->NULL")
        self.assertEqual(x.data, 10)
        x = self.testList.pop()
        self.assertEqual(str(self.testList), "NULL")
        self.assertIsNone(self.testList.head)
        self.assertEqual(x.data, 5)


if __name__ == "__main__":
    unittest.main()
