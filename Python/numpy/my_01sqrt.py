import numpy as np
import time,math
lst2 = []
# lst = [2,3,1,34,543,2313,543,545656,56,34,534,5,45,345,435,43,23,654,6765,34,2,3867,2,3,1,34,543,2313,543,545656,56,34,534,5,45,345,435,43,23,654,6765,34,2,3867,2,3,1,34,543,2313,543,545656,56,34,534,5,45,345,435,43,23,654,6765,34,2,3867]
# for i in lst:
#     lst2.append(math.sqrt(i))
# print(lst2)
# print(np.sqrt(lst))
# print(time.process_time())
arr = np.random.randint(0,6,(10,10))
print(arr)
print(arr[0:10:2,0:10:2])