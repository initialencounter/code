def yezi(i):
    i = ((i - 1) * 2) / 3
    i = ((i - 1) * 2) / 3
    i = ((i - 1) * 2) / 3
    return  i
def main():
    i = 1
    while 1:
        n = yezi(i)
        if int(n)==n and (n-1)%3==0:
            break
        else:
            i+=1
    print(i)
if __name__ == '__main__':
    main()

def duitao():
    i = 6
    while 1:
        n = i
        for x in range(5):
            n = ((n - 1) * 4) / 5
        if int(n)==n:
            break
        else:
            i+=1
    print(i)
duitao()
def woniu():
    n = 0
    i = 0
    while 1:
        n += 1.0
        i+=1
        if n>=9.8:
            break
        else:
            n-=0.78

    print(i)
woniu()
def gold():
    g = 1
    i = 2
    n = 365
    while 1:
        n=n-i
        z = i
        i+=1
        if n>=0:
            g = g + z*z
        else:
            g= (n-1+z)*(z)+g
            break

    print(g)
gold()
def yinliao():
    n = 80
    nzong =n
    while n>3:
        n1 = n
        nhuan = n//3
        nhuan2 = nhuan+(n1-nhuan*3)
        nzong += nhuan
        n = nhuan2
    print(nzong)

yinliao()

def rt_run(endt):
    r = 9
    t = 3
    time = 1
    while time<endt:
        if t>=r:
            r +=9
            t +=3
            time+=1
        else:
            x = endt-(time+30)
            print(x)
            if x>0:
                t+=3*30
                time+=30
            else:
                t+=(endt-time)*3
                time=endt
    print(r, t)
    if r>t:
        print('兔子获胜')
    elif r<t:
        print('乌龟获胜')
    else:
        print('平局')
rt_run(46)

def micocell():
    x= 10
    y=90
    for time in range(120):
        if time%2==1:
            y=y-x
        if time%6==0:
            x+=x
        if time%4==0:
            y+=y
    print(y)
micocell()
