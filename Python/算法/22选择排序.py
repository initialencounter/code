a=[1,5,4,2,8,7,1,6,4,8]
def shuangchong():
    j=0
    while j<=len(a)-1:
        p=j
        i=j+1
        while i<len(a):
            if a[i]<a[p]:
                p=i
            i+=1
        if p!=j:
            a[j],a[p]=a[p],a[j]
        j+=1
        print(a)
# shuangchong()
def max_():
    p=0
    i=p+1
    while i<len(a):
        if a[i]>a[p]:
            p=i
        i+=1
    print(a[p])

#max_()
def m_for():
    for j in range(len(a)):
        p=j
        i=j+1
        for i in range(i,len(a)):
            if a[i]<a[p]:
                p=i
        if p!=j:
            a[p],a[j]=a[j],a[p]
        print(a)
m_for()