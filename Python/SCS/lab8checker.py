import unittest
import lab8
from io import StringIO
"""
This chacker can only check if the code you write is correct or not.
However, while solving the problem, do not forget the limitations.
"""

final = [[[77, 99, 99, 48, 31],
          [96, 63, 10, 36, 7],
          [11, 66, 5, 72, 32],
          [74, 99, 14, 5, 35]],
         [[1, 37, 55, 33, 45, 98, 36],
          [90, 1, 57, 95, 88, 56, 81],
          [35, 11, 75, 11, 35, 38, 85],
          [46, 3, 51, 49, 73, 17, 90],
          [27, 99, 93, 58, 18, 30, 65],
          [91, 59, 14, 15, 82, 72, 3]]]
final2 = [[[2,2,3],
           [3,2,4]],
          [[4,2],
           [1,2]],
          [[2,2],
           [3,2],
           [4,2]],
          [[1,2,3],
           [4,5,6],
           [7,8,9],
           [22,33,44]]]
f = open('sample_data.csv')
test = """4
2,3
2,2
3,2
4,3
2,2,3
3,2,4
4,2
1,2
2,2
3,2
4,2
1,2,3
4,5,6
7,8,9
22,33,44

"""
test1 = ['4\n2,3\n2,2\n3,2\n4,3\n2,2,3\n3,2,4\n4,2\n1,2\n2,2\n3,2\n4,2\n1,2,3\n4,5,6\n7,8,9\n22,33,44\n']
f1 = open('csc108checker.csv', 'w')
case1 = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]
class TestProblem(unittest.TestCase):


    def test_get_elevation_maps(self):
        self.assertEqual(lab8.get_elevation_maps(f), final)
        f.close()
        self.assertEqual(lab8.get_elevation_maps(StringIO(test)), final2)


    def test_write_elevation_maps(self):
        lab8.write_elevation_maps(f1, final2)
        f1.close()
        f2 = open('csc108checker.csv')
        new = f2.read()
        self.assertEqual(new, test1[0])
        f2.close()


    def test_crop_map(self):
        new = case1[:]
        self.assertEqual(lab8.crop_map(case1, (1, 1), (2, 3)), [[6, 7, 8], [10, 11, 12]])
        self.assertEqual(lab8.crop_map(case1, (2, 3), (1, 1)), [[6, 7, 8], [10, 11, 12]])
        self.assertEqual(lab8.crop_map(case1, (1, 3), (2, 3)), [[8], [12]])
        self.assertEqual(lab8.crop_map(case1, (2, 3), (1, 3)), [[8], [12]])
        self.assertEqual(lab8.crop_map(case1, (1, 1), (1, 1)), [[6]])
        self.assertEqual(lab8.crop_map(case1, (3, 3), (3, 0)), [[13, 14, 15, 16]])
        self.assertEqual(lab8.crop_map(case1, (3, 0), (3, 3)), [[13, 14, 15, 16]])
        self.assertEqual(lab8.crop_map(case1, (0, 0), (3, 3)), case1)
        self.assertEqual(lab8.crop_map(case1, (0, 3), (3, 0)), case1)
        self.assertEqual(lab8.crop_map(case1, (1, 2), (2, 1)), [[6, 7], [10, 11]])
        self.assertEqual(new, case1)
        

    def test_rotate_map(self):
        new = case1[:]
        self.assertEqual(lab8.rotate_map(case1, 'right'), [[13, 9, 5, 1], [14, 10, 6, 2], [15, 11, 7, 3], [16, 12, 8, 4]])
        self.assertEqual(lab8.rotate_map(case1, 'left'), [[4, 8, 12, 16], [3, 7, 11, 15], [2, 6, 10, 14], [1, 5, 9, 13]])
        self.assertEqual(new, case1)
        self.assertEqual(lab8.rotate_map([[1]], 'right'), [[1]])
        self.assertEqual(lab8.rotate_map([[1]], 'left'), [[1]])



        
if __name__ == '__main__':
    unittest.main()
