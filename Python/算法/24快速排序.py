import sys,time
def move(j,k,i):
    while 1:
        while i > k:
            if a[i] >= a[j]:
                i -= 1
            else:
                break
        while k < i:
            if a[k] <= a[j]:
                k += 1
            else:
                break
        if k==i:
            a[k], a[j] = a[j], a[k]
            break
        else:
            a[k], a[i] = a[i], a[k]
    return j,k
def recursion(j,i):
    j1 = j[0]
    j2 = j[1]+1
    k1 = j[0]
    k2 = j[1] + 1
    i1 = j[1] - 1
    i2 = i
    if i1-k1>0:
        j = move(j1,j1,i1)
        recursion(j,i1)
    if i2-k2>0:
        j = move(j2,k2,i2)
        recursion(j,i2)
    print(a)
def main():
    sys.setrecursionlimit(100000000)
    global a
    a = [1,4,2,5,7,8,6,3]
    i = len(a) - 1
    j = 0
    k = j
    j = move(j, k, i)
    recursion(j, i)
    print(time.process_time())
# main()
def partition(a,left,right):
    base = left
    while left<right:
        while left<right and a[right]>=a[base]:
            right-=1
        while left<right and a[left]<=a[base]:
            left+=1
        a[left],a[right]=a[right],a[left]
    a[left],a[base]=a[base],a[left]
    return left
def quicksort(a,left,right):
    if left<right:
        base = partition(a,left,right)
        print(base,a)
        quicksort(a,left,base-1)
        quicksort(a,base+1,right)
def sort_0():
    a=[1,4,2,5,7,8,6,3]
    quicksort(a,0,len(a)-1)
sort_0()

