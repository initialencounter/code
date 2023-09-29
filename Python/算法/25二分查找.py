def binary_search(n,a):
    left = 0
    right = len(a)
    while left<=right:
        index = int((right-left)//2+left)
        if a[index]==n:
            return index
        elif a[index]<n:
            left=index+1
        elif a[index]>n:
            right=index-1
    return -1

# print(binary_search(1,a))




def recursion_binary_seacrh(n,a,left,right):
    if left<=right:
        mid = int((right - left) // 2 + left)
        if a[mid] == n:
          return mid
        elif a[mid] < n:
            recursion_binary_seacrh(n, a,  mid+1,right)
        else:
            recursion_binary_seacrh(n,a,left,mid-1)
    else:
        return -1
a=[1,2,5,7,9,13]
print(recursion_binary_seacrh(2,a,0,len(a)-1))