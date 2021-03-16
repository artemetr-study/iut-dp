import unittest

from lw_1.linear_comparison import linear_comparison


class LinearComparisonTestCase(unittest.TestCase):
    test_cases = [
        [7, 5, 19, 17],
        [5, 4, 21, 5],
        [11, 17, 119, 34],
        [12, 8, 67, 23]
    ]

    def test_results(self):
        for case in self.test_cases:
            self.assertEqual(linear_comparison(case[0], case[1], case[2]), case[3])


if __name__ == '__main__':
    unittest.main()
