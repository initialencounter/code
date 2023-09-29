def meiju():
    x=1
    while True:
        y=x-18
        if (x+9) == 2*(y-9):
            print(x,y)
            break
        else:
            x+=1
# meiju()
# 买酒
def 买酒():
    x=1
    while True:
        y = 3*(200-x)
        if y+0.5*x==200:
            print(x,y)
            break
        else:
            print(x)
            x+=1
def sheep():
    x = 1
    while 1:
        y = 70-x
        if x* 1.6 +y*1.2==106:
            print(x,y)
            break
        else:
            x+=1
def duck():
    x= 1
    while 1:
        y = 2 *x
        if 3*(x-6) == y-8:
            print(x,y)
            break
        else:
            x+=1

def money() :
    x=1
    while 1:
        y=1000-x
        if (11*x/9) +(4*y/7) == 999 :
            print(x,y)
            break
        else:
            print(x)
            x+=1


def sake() :
    x=1
    while 1:
        y=19-x
        if (3*x) +(y/3) == 33 :
            print(x,y)
            break
        else:
            print(x)
            x+=1
def chicken() :
    x=1
    while x<100:
        e = 0
        while e<100:
            y=100-x
            z = y-e
            if (x*5) +(e*3)+(z/3) == 100 :
                print(x,e,z)
                x=102
            else:
                e+=1
        x+=1







lst = []
lst_lst = []
for i in range(1,7):
    for j in range(1,7):
        for k in range(1,7):
            for l in range(1,7):
                for m in range(1,7):
                    for n in range(1,7):
                        if len(set((i,j,k,l,m,n)))==6:
                            lst=[i,j,k,l,m,n][:]
                            if lst[0]<lst[1]<lst[2] and lst[5]<lst[4]<lst[3]:
                                if lst not in lst_lst:
                                    lst_lst.append(lst)
count1 = 0
for i in lst_lst:
    count=0
    for j in i:
        count+=1
        if count==4:
            print(7,end='')
        print(j,end='')
    print('    ',end='')
    count1+=1
    if count1%5==0:
        print()
print()
print(len(lst_lst))
