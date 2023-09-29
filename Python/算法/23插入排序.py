# a=[7,11,3,2,5]
# j=1
# while j<len(a):
#     i=j
#     while i>0:
#         if a[i]<a[i-1]:
#             a[i],a[i-1] = a[i-1],a[i]
#             i -=1
#         else:
#             i=0
#         print(a)
#     j+=1
# a= [2, 3, 7, 11]
# n=9
# a.append(n)
# i=len(a)-1
# while i>0:
#     if a[i]<a[i-1]:
#         a[i],a[i-1]=a[i-1],a[i]
#         i-=1
#     else:
#         i=0
#
# print(a)


a=[11, 7, 3, 2, 5]
for j in range(len(a)):
    for i in range(j,0,-1):
        if a[i]<a[i-1]:
            a[i],a[i-1]=a[i-1],a[i]
            i-=1
        else:
            i=0
print(a)












