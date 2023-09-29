import unittest
import lab5
"""
 check
"""
class TestProblem(unittest.TestCase):


    def test_sum_string(self):
        self.assertEqual(lab5.sum_string(''), 0)
        self.assertEqual(lab5.sum_string('54321'), 3)
        self.assertEqual(lab5.sum_string('0000'), 0)
        self.assertEqual(lab5.sum_string('00009'), 9)
        self.assertEqual(lab5.sum_string('0009'), -9)
        self.assertEqual(lab5.sum_string('133'), 1)
        self.assertEqual(lab5.sum_string('1'), 1)
        self.assertEqual(lab5.sum_string('23'), -1)


    def test_substring_with_largest_sum(self):
        self.assertEqual(lab5.substring_with_largest_sum("321"), '3')
        self.assertEqual(lab5.substring_with_largest_sum(''), '')
        self.assertEqual(lab5.substring_with_largest_sum('444'), '4')
        self.assertEqual(lab5.substring_with_largest_sum('004'), '004')
        self.assertEqual(lab5.substring_with_largest_sum('2034'), '203')
        self.assertEqual(lab5.substring_with_largest_sum('2035'), '203')
        self.assertEqual(lab5.substring_with_largest_sum('00009'), '00009')
        self.assertEqual(lab5.substring_with_largest_sum('90000'), '9')


    def test_loopy_madness(self):
        self.assertEqual(lab5.loopy_madness('a', 'c'), 'ac')
        self.assertEqual(lab5.loopy_madness('ac', 'bd'), 'abcd')
        self.assertEqual(lab5.loopy_madness('ab', 'c'), 'acbc')
        self.assertEqual(lab5.loopy_madness('c', 'ab'), 'cacb')
        self.assertEqual(lab5.loopy_madness('c', 'abbbbbbbbbbbbbbbbbbbbb' + 'b' * 10000), 'cacbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcb' + 'cb' * 10000)
        self.assertEqual(lab5.loopy_madness('abbbbbbbbbbbbbbbbbbbbb' + 'b' * 10000, 'c'), 'acbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbc' + 'bc' * 10000)
        self.assertEqual(lab5.loopy_madness('abcd', 'ef'), 'aebfcedf')
        self.assertEqual(lab5.loopy_madness('abcd', 'efg'), 'aebfcgdf')
        self.assertEqual(lab5.loopy_madness('abcdfe', '123'), 'a1b2c3d2f1e2')

if __name__ == '__main__':
    unittest.main()
