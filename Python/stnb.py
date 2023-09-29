def compute(target=None):
    if target==None:
        target = input('输入time bvs grade：')
    time,bvs,grade = target.split(' ')
    if grade == '1':
        cont = 47.229
    elif grade == '2':
        cont = 153.73
    else:
        cont = 435.001
    return cont / ((float(time) ** 1.7) / (float(time) * float(bvs)))

print(compute(input("请输入t[bvs][grade]:")))
