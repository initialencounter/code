import unittest
import lab7
"""
for self check and practice only.
Before you starting doing the lab. I should also inform you that the lab this
week will really be a challenge for you guys. Do not be panic if you cannot
solve it, it is just a practice.
"""
case1 = [[1, 0, 1, 0, 0],
         [1, 0, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]
case2 = [[1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1]]
case3 = [[1, 1, 1, 0, 0],
         [1, 1, 1, 0, 0],
         [1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0]]
case4 = [[1, 1, 1, 0, 0],
         [1, 1, 1, 0, 0],
         [1, 1, 1, 1, 0],
         [1, 1, 1, 1, 1]]
class TestProblem(unittest.TestCase):


    def test_longest_chain(self):
        self.assertEqual(lab7.longest_chain([1, 1, 0]), 2)
        self.assertEqual(lab7.longest_chain([]), 0)
        self.assertEqual(lab7.longest_chain([1, 1, 1, 1, 0, 1]), 4)
        self.assertEqual(lab7.longest_chain([0, 0, 0, 1, 1, 1]), 0)
        self.assertEqual(lab7.longest_chain([0, 0, 0, 0, 0]), 0)
        self.assertEqual(lab7.longest_chain([1, 1, 1, 1]), 4)
        self.assertEqual(lab7.longest_chain([1, 0, 1, 1]), 1)
        self.assertEqual(lab7.longest_chain([1, 1, 0, 1, 1]), 2)


    def test_largest_at_position(self):
        self.assertEqual(lab7.largest_at_position(case1, 0, 0), 4)
        self.assertEqual(lab7.largest_at_position(case1, 2, 0), 5)
        self.assertEqual(lab7.largest_at_position(case1, 1, 2), 6)
        self.assertEqual(lab7.largest_at_position(case1, 0, 1), 0)
        self.assertEqual(lab7.largest_at_position(case1, 3, 3), 1)
        self.assertEqual(lab7.largest_at_position(case2, 0, 0), 20)
        self.assertEqual(lab7.largest_at_position(case2, 0, 0), 20)
        self.assertEqual(lab7.largest_at_position(case3, 0, 0), 8)
        self.assertEqual(lab7.largest_at_position(case4, 0, 0), 12)

    def test_largest_in_matrix(self):
        self.assertEqual(lab7.largest_in_matrix(case1), 6)
        self.assertEqual(lab7.largest_in_matrix(case2), 20)
        self.assertEqual(lab7.largest_in_matrix(case3), 8)
        self.assertEqual(lab7.largest_in_matrix(case4), 12)


if __name__ == '__main__':
    unittest.main()
