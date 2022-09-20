import unittest
from code.merge_dicts import join_dicts_values_as_list, join_list_of_dicts


class TestJoinListOfDicts(unittest.TestCase):
    def test_case1(self):
        l1 = [{"index": 1, "b": 2}, {"index": 2, "b": 3}, {"index": 3, "green": "eggs"}]
        l2 = [{"index": 1, "c": 4}, {"index": 2, "c": 5}]
        l3 = join_list_of_dicts(l1, l2)
        self.assertEqual(
            l3,
            [
                {"index": 1, "b": 2, "c": 4},
                {"index": 2, "b": 3, "c": 5},
                {"index": 3, "green": "eggs"},
            ],
        )
        self.assertListEqual(
            l3,
            [
                {"index": 1, "b": 2, "c": 4},
                {"index": 2, "b": 3, "c": 5},
                {"index": 3, "green": "eggs"},
            ],
        )
        self.assertDictEqual(l3[0], {"index": 1, "b": 2, "c": 4})
        self.assertDictEqual(l3[1], {"index": 2, "b": 3, "c": 5})
        self.assertDictEqual(l3[2], {"index": 3, "green": "eggs"})

    def test_case2(self):
        l1 = [{"pig": 1, "cow": 2}, {"pig": 2, "parrot": 3}, {"pig": 3, "dog": 8}]
        l2 = [{"pig": 1, "monkey": 4}, {"pig": 2, "dog": 5}]
        l3 = join_list_of_dicts(l1, l2, "pig")
        self.assertEqual(
            l3,
            [
                {"pig": 1, "cow": 2, "monkey": 4},
                {"pig": 2, "parrot": 3, "dog": 5},
                {"pig": 3, "dog": 8},
            ],
        )
        self.assertListEqual(
            l3,
            [
                {"pig": 1, "cow": 2, "monkey": 4},
                {"pig": 2, "parrot": 3, "dog": 5},
                {"pig": 3, "dog": 8},
            ],
        )
        self.assertDictEqual(l3[0], {"pig": 1, "cow": 2, "monkey": 4})
        self.assertDictEqual(l3[1], {"pig": 2, "parrot": 3, "dog": 5})
        self.assertDictEqual(l3[2], {"pig": 3, "dog": 8})

    """ def test_case3(self):
        pass

    def test_case4(self):
        pass

    def test_case5(self):
        pass """


class TestdefJoinDictsValuesAsList(unittest.TestCase):
    def test_case1(self):
        d1 = {"pig": 1, "cow": 2, "parrot": 3, "monkey": 4}
        d2 = {"pig": 5, "cow": 8, "parrot": 5, "dog": 4}
        d3 = join_dicts_values_as_list(d1, d2)
        self.assertEqual(
            d3,
            {"pig": [1, 5], "cow": [2, 8], "parrot": [3, 5], "monkey": [4], "dog": [4]},
        )
        self.assertDictEqual(
            d3,
            {"pig": [1, 5], "cow": [2, 8], "parrot": [3, 5], "monkey": [4], "dog": [4]},
        )
        self.assertListEqual(d3["pig"], [1, 5])
        self.assertListEqual(d3["cow"], [2, 8])
        self.assertListEqual(d3["parrot"], [3, 5])
        self.assertListEqual(d3["monkey"], [4])


if __name__ == "__main__":
    unittest.main()
