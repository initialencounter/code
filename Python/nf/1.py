#读取数组
lis = [[0,1,9,9,9,2,0,0,0],
       [1,1,9,9,1,3,0,0,0],
       [9,9,9,9,2,0,0,0,0],
       [9,9,9,9,2,0,0,0,0],
       [9,9,9,9,1,1,1,1,1]]
#格式化
lst1 = [[9,9,9,9,9,9,9,9,9,9,9]]
for i in lis:
    j = [9]+i+[9]
    lst1.append(j)
lst1.append([9,9,9,9,9,9,9,9,9,9,9])
# lst1 = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
#         [9, 0, 1, 9, 9, 9, 2, 0, 0, 0, 9],
#         [9, 1, 1, 9, 9, 1, 3, 0, 0, 0, 9],
#         [9, 9, 9, 9, 9, 2, 0, 0, 0, 0, 9],
#         [9, 9, 9, 9, 9, 2, 0, 0, 0, 0, 9],
#         [9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 9],
#         [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]
#计算
def cout(y,x,lst1):
    #0，8分别代表：未知，雷
    mine = 0
    unknow = 0
    unknow_lst = []
    lst3 = [-1,0,1]
    for i in lst3:
        for j in lst3:
            if i==j and i==0:
                print(1)
            else:
                num = lst1[y+i][x+j]
                if num==0:
                    unknow+=1
                    unknow_lst.append([y+i,x+j])
                elif num==8:
                    mine+=1
    if unknow+mine == lst1[y][x]:
        for i in unknow_lst:
            lst1[i[0]][i[1]]=8
    print(unknow)
    print(unknow_lst)
    print(lst1)
    return lst1
for y in range(1,6):
    for x in range(1,10):
        if lst1[y][x] != 8:
            lst1 = cout(y,x,lst1)

lst1 = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
        [9, 8, 1, 9, 9, 9, 2, 8, 0, 0, 9],
        [9, 1, 1, 9, 9, 1, 3, 8, 0, 0, 9],
        [9, 9, 9, 9, 9, 2, 8, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 2, 8, 0, 0, 0, 9],
        [9, 9, 9, 9, 9, 1, 1, 1, 1, 1, 9],
        [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]
