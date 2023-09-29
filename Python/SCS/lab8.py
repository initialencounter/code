"""
LAB RESTRICTIONS, PLEASE READ:
Do not add any imports, the ones that you need will be given to you.
You may not use any dictionaries or dictionary methods.
Do not use try-except statements, you should be able to anticipate
or prevent any errors from happening at all!
"""
import csv

from typing import TextIO

# def get_elevation_maps(maps_file: TextIO) -> list[list[list[int]]]:
def get_elevation_maps(maps_file):
    """
    Given an open csv file <maps_file>, read the file according to the
    specification and return all the elevation maps stored within the file.

    IMPORTANT: the given argument to the function is an OPEN file <maps_file>,
    you will not need to open it again, and can begin performing standard file
    operations on it.

    The file will be structured as follows:
        - The first line will contain one number, which will denote the number
          of elevation maps stored within this file.
        - The next n lines will contain two numbers each, "r" and "c", which
          are the number of rows and columns of each elevation map.
        - The rest of the data will then be comprised of the elevation map
          data, which will follow one another in sequence, with no spaces in
          between.

    For an example, see "sample_data.csv".
    """
    lst1 = []
    lst3 = []
    #读取cvs文件，写入lst1
    for row in maps_file:
        row  = row.replace('\n','')#str to list
        row = row.split(',')
        lst1.append(row)
    num1=int(lst1[0][0])
    num_l=lst1[1:num1+1]
    num2 = 0#len of second line
    num3 = 0#len of the third line
    lst4 = []
    for num in num_l:
        lst4.append(int(num[0]))
        num2+=1
        num3+=int(num[0])

    # subsript
    lst2=lst1[1+num2:1+num2+num3]

    #str to int
    for i in lst2:
        for j in range(len(i)):
            i[j]=int(i[j])
        lst3.append(i)

    #lst3按照lst4分类，即将长度相等的子列表放在同一个列表
    a=0
    lst5=[]
    for i in lst4:
        i+=a
        lst5.append(lst3[a:i])
        a=i

    return  lst5
# f = open('sample_data.csv','r')
# print(get_elevation_maps(f))
# f.close()
# def write_elevation_maps(maps_file: TextIO, maps_list: list[list[list[int]]]
#                          ) -> None:
def write_elevation_maps(maps_file,maps_list):
    """
    Given an open csv file <maps_file> and a list of maps <maps_list>, write
    the maps back into the csv file according to the format specified in
    <get_elevation_maps>. That is, if the same file was then read from again
    by the <get_elevation_maps> function, it should return a list identical
    to <maps_list>.

    IMPORTANT: <maps_file> is an already open file, you can begin writing to it
               immediately. Furthermore, DO NOT close the file <maps_file>
               after you are finished writing the data in.
    """
    line1 = [[len(maps_list)]]
    line2= []
    line3 = []
    for i in range(len(maps_list)):
        line2.append([len(maps_list[i]),len(maps_list[i][0])])
        for j in maps_list[i]:
            line3.append(j)
    row_lst = line1+line2+line3

    # 将row_lst写入map_file
    for i in row_lst:
        f_csv = csv.writer(maps_file)
        f_csv.writerow(i)
    # print(row_lst)

m = [[[2,2,3],
      [3,2,4]],
     [[4,2],
      [1,2]],
     [[2,2],
      [3,2],
      [4,2]],
     [[1,2,3],
      [4,5,6],
      [7,8,9],
      [22,33,44]]]
# f = open('test.csv','w')
# print(write_elevation_maps(f, m))
# f.close()


# def crop_map(m: list[list[int]], corner_1: tuple[int, int],
#              corner_2: tuple[int, int]) -> list[list[int]]:
def crop_map(m,corner_1,corner_2):
    """
    Given a 2D representation of an elevation map <m> and two points on the map
    <corner_1> and <corner_2>, crop the map and return the smallest map such
    that both these coordinates are now a corner on the new map.

    Note that the new cropped map could just be a row, a column, or even a
    single square like [[1]]. The new map must remain rectangular, that is,
    each of its rows must be equal in length.

    Do not modify the original map.

    # >>> sample_map = [[1, 2, 3, 4],
    # ...               [5, 6, 7, 8],
    # ...               [9, 10, 11, 12],
    # ...               [13, 14, 15, 16]]
    #
    # >>> crop_map(sample_map, (1, 1), (2, 2))
    # [[6, 7], [10, 11]]
    # >>> crop_map(sample_map, (0, 0), (3, 0))
    # [[1], [5], [9], [13]]
    # >>> crop_map(sample_map, (0, 3), (0, 0))
    # [[1, 2, 3, 4]]
    # """
    #y1,x1,y2,x2

    row1,col1,row2,col2 = corner_1[0],corner_1[1],corner_2[0],corner_2[1]
    lst1 =[]
    # 计算出要剪切矩形的左上角坐标与矩形的宽和高，左上角坐标即col1，col2中最小的值与row1，row2中最小的值
    # 左上角坐标行(x,y)与宽w高h
    if row2>row1:
        y = row1
        h = row2-row1+1
    else:
        y = row2
        h = row1-row2+1
    if col2>col1:
        x = col1
        w = col2-col1+1
    else:
        x = col2
        w = col1-col2+1

    #剪切
    for i in range(len(m)):
        if y<=i<y+h:
            lst1.append(m[i][x:x+w])
    return  lst1


# sample_map = [[1, 2, 3, 4],
#              [5, 6, 7, 8],
#              [9, 10, 11, 12],
#              [13, 14, 15, 16]]
# print(crop_map(sample_map,(2,3),(1,1)))


# def rotate_map(m: list[list[int]], direction: str) -> list[list[int]]:
def rotate_map(m,direction):
    """
    Given a 2D representation of an elevation map <m>, rotate the map either
    to the right or to the left, depending on the <direction>. A rotation will
    be 90 degrees in the direction specified.

    Do not modify the original map.

    For example:
    # >>> rotate_map([[1, 2], [3, 4]], 'left')
    [[2, 4], [1, 3]]
    """
    #根据子列表的长度，创建旋转后的空列表lst[[],
    #                                  [],
    #                                  [],
    #                                  []]
    lst = []
    for i in range(len(m[0])):
        lst.append([])
        for j in range(len(m)):
            lst[i].append([])
    #在空列表中添加旋转后的数字
    '''
            [1,2]                    [2,4,6]
            [3,4]   left rotated --> [1,3,5]
            [5,6] 
            
            step1:  [[,,],     step2:    [[2,,],     step3:   [[2,,],
                     [,,]]                [,,]]               [1,,]]
            step4:  [[2,4,],   step5:    [[2,4,],    step6:   [[2,4,5],
                     [1,,]]               [1,3,]]              [1,3,]]
            step7:  [[2,4,5],
                     [1,3,6]]
    '''
    if direction == 'left':
        for i in range(len(m[0])):
            for j in range(len(m)):
                lst[i][j] = m[j][::-1][i]

    elif direction == 'right':
        for i in range(len(m[0]))[::-1]:
            for j in range(len(m)):
                lst[i][j] = m[len(m[0]) - 1 - j][i]
    return lst
# m=[[1,2,3,4,],
#    [5,6,7,8],
#    [9,10,11,12],
#    [13,14,15,16]]
# print(rotate_map(m,'left'))