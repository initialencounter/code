import unittest
import lab6
"""
lab 6 cheecker(For practice only)
"""
class TestProblem(unittest.TestCase):


    def test_longest_chain(self):
        self.assertEqual(lab6.longest_chain([1, 1, 0]), 2)
        self.assertEqual(lab6.longest_chain([]), 0)
        self.assertEqual(lab6.longest_chain([1, 1, 1, 1, 0, 1]), 4)
        self.assertEqual(lab6.longest_chain([0, 0, 0, 1, 1, 1]), 0)
        self.assertEqual(lab6.longest_chain([0, 0, 0, 0, 0]), 0)
        self.assertEqual(lab6.longest_chain([1, 1, 1, 1]), 4)
        self.assertEqual(lab6.longest_chain([1, 0, 1, 1]), 1)
        self.assertEqual(lab6.longest_chain([1, 1, 0, 1, 1]), 2)


    def test_second_largest(self):
        self.assertEqual(lab6.second_largest([1, 1, 0]), 1)
        self.assertEqual(lab6.second_largest([2, 3]), 2)
        self.assertEqual(lab6.second_largest([1, 2, 4, 5, 6, 7]), 6)
        self.assertEqual(lab6.second_largest([0, 0, 0, 1, 1, 1]), 1)
        self.assertEqual(lab6.second_largest([0, 0, 0, 0, 0]), 0)
        self.assertEqual(lab6.second_largest([1, 1, 1, 1, 0]), 1)
        self.assertEqual(lab6.second_largest([1, 0, 1, 1]), 1)
        self.assertEqual(lab6.second_largest([7, 6, 5, 4, 3, 2, 1]), 6)

    def test_count_types(self):
        self.assertEqual(lab6.count_types([1, 1, 0]), [3])
        self.assertEqual(lab6.count_types([1, 1, 0.0]), [2, 1])
        self.assertEqual(lab6.count_types([0.0, 1, 1]), [1, 2])
        self.assertEqual(lab6.count_types([0.0, 1, True, [], {}, ()]), [1, 1, 1, 1, 1, 1])
        self.assertEqual(lab6.count_types([1, 'Haocheng', 34, 'Leila', True]), [2, 2, 1])
        self.assertEqual(lab6.count_types([]), [])


    def test_loopy_madness_with_while_loops(self):
        self.assertEqual(lab6.loopy_madness_with_while_loops('a', 'c'), 'ac')
        self.assertEqual(lab6.loopy_madness_with_while_loops('ac', 'bd'), 'abcd')
        self.assertEqual(lab6.loopy_madness_with_while_loops('ab', 'c'), 'acbc')
        self.assertEqual(lab6.loopy_madness_with_while_loops('c', 'ab'), 'cacb')
        self.assertEqual(lab6.loopy_madness_with_while_loops('c', 'abbbbbbbbbbbbbbbbbbbbb' + 'b' * 100000), 'cacbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb' + 'cb' * 100000)
        self.assertEqual(lab6.loopy_madness_with_while_loops('abbbbbbbbbbbbbbbbbbbbb' + 'b' * 100000, 'c'), 'acbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc' + 'bc' * 100000)
        self.assertEqual(lab6.loopy_madness_with_while_loops('abcd', 'ef'), 'aebfcedf')
        self.assertEqual(lab6.loopy_madness_with_while_loops('abcd', 'efg'), 'aebfcgdf')
        self.assertEqual(lab6.loopy_madness_with_while_loops('abcdfe', '123'), 'a1b2c3d2f1e2')

if __name__ == '__main__':
    unittest.main()
