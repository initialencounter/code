from fiv_3 import best
import time
lst = [3,3,8,9,12,15]
lst2 = []
for i in range(6):
    s = lst[0]
    lst.remove(s)
    lst2.append(best(lst))
    lst.append(s)
print(lst2,time.process_time())
