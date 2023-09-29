def maopao():
    list1=[6,2,3,1,4,5]
    i=1
    j=len(list1)-1
    while len(list1)-1 >= i:
        j=len(list1)-1
        while j>=i:
            if list1[j]<list1[j-1]:
                list1[j],list1[j-1]=list1[j-1],list1[j]
            j -= 1
        print(list1)
        i+=1
# maopao()











def m2():
    l = [12,1,4,6,5745,88,54]
    j=1
    while j<=len(l)-1:
        i = len(l)-1
        while j<=i:
            if l[i]>l[i-1]:
                l[i],l[i-1]=l[i-1],l[i]
            i-=1
        print(l)
        j+=1
    print(l[0])
# m2()
def m3():
    l = [12,1,4,6,5745,88,54]
    j=1
    i = len(l)-1
    while j<=i:
        if l[i]>l[i-1]:
            l[i],l[i-1]=l[i-1],l[i]
        i-=1
        print(l)
    j+=1
    print(l[0])
# m3()
def m4():
    l = [12,1,499,6,574,5,88,54]
    j=1
    while 1:
        i = len(l) - 1
        swap=1
        while j<=i:
            if l[i]>l[i-1]:
                l[i],l[i-1]=l[i-1],l[i]
                swap=0
            i-=1
        if swap==1:
            break
        print(l)
        j+=1
m4()
import time
print(time.process_time())