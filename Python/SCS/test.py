# items = [1,9,4,2,3]
# def first_even(items):
#     for i in items:
#         if i%2==0:
#             return i
#     return -1
# print(first_even(items))



# def sum_string(str_)-> int:
#
#     sum = 0
#     if str_ ==None:
#         return sum
#     for i in range(len(str_)):
#         if int(i) % 2 == 0:
#             sum += int(str_[i])
#         else:
#             sum -= int(str_[i])
#     return sum

# s = '12345'
# largest = 0
# for step in range(len(s)):
#     step += 1
#     id = 0
#     for j in range(len(s)):
#         if id + step > len(s):
#             pass
#         j = s[id:id + step]
#         l = sum_string(j)
#         if l > largest: largest = l
#         id += 1
# print(j)
# def main():
#     str2 = 'abcdefghjkl'
#     str1 ='1234'
#     id = 0
#     inter = ''
#     direct = 0
#     transf = len(str1)-1
#     for i in range(len(str2)):
#         inter += (str1[id]+str2[i])
#         if i%transf==0:
#             if direct==1:
#                 direct=0
#             else:
#                 direct=1
#         if direct==1:
#             id+=1
#         else:
#             id-=1
#     print(inter)
# main()
# def sum_string(str_)-> int:
#
#     sum = 0
#     if str_ ==None:
#         return sum
#     for i in range(len(str_)):
#         if int(i) % 2 == 0:
#             sum += int(str_[i])
#         else:
#             sum -= int(str_[i])
#     return sum


# def substring_with_largest_sum(str_) -> str:
#     largest = 0
#     if str_ =='':
#         return ''
#     for step in range(len(str_)):
#         if str_[0] =='0':
#             step = len(str_) - step
#         id = 0
#         for j in range(len(str_)):
#             if id + step > len(str_):
#                 continue
#             j = str_[id:id + step]
#             k = sum_string(j)
#             print(j)
#             if k > largest:
#                 largest = k
#                 largest_str = j
#             id += 1
#     return largest_str
# print(substring_with_largest_sum('444'))
# # substring_with_largest_sum('004')
# # if substring_with_largest_sum('321')=='3':
# #     print(1)
#
# print(sum_string('203'))
# def search_closet(items,colour):
#     new = []
#     for item in items:
#         item_color = item.split(' ')[0]
#         if colour in item_color:
#             if item not in new:
#                 new.append(item)
#     return new
# print(search_closet(['red summer jacket', 'orange spring jacket','red shoes', 'green hat'], 'red'))


# string = 'red summer jacket orange spring jacket red shoes green hat'
# print(string.split(' '))
# def substring_with_largest_sum1(s) -> str:
#     largest = 0
#     if s =='':
#         return ''
#     for i in range(len(s)):
#         for j in range(len(s[i:])):
#             j = s[i:][:j+1]
#             k = sum_string(j)
#             if k > largest:
#                 largest = k
#                 largest_str = j
#     return largest_str
# print(substring_with_largest_sum1('444'))
#
# str1 = '12345678'
# str2 = 'a'
# # str3 = ''
# str4 = ''
# inter = ''
# id = 0
# if len(str2)==1:
#     for i in str1:
#         inter += (str1[i] + str2)
# elif len(str1)==1:
#     for i in str2:
#         inter += (str1 + str2[i])
# if len(str2)>len(str1):
#     for i in range(len(str2)):
#         str4 += str1[id]
#         if i%(2*(len(str1)-1)) <(len(str1)-1):
#             id += 1
#         else:
#             id -= 1
#     for i in str2:
#         inter += (str1[i] + str4[i])
# elif len(str1)>len(str2):
#     for i in range(len(str1)):
#         str4 += str2[id]
#         if i%(2*(len(str2)-1)) <(len(str2)-1):
#             id += 1
#         else:
#             id -= 1
#     for i in str1:
#         inter += (str1[i] + str4[i])
#
# elif len(str1)==len(str2):
#     for i in str1:
#         inter += (str1[i] + str2[i])
#
# # print(str4)
#
# print(inter)





# def loopy_madness(str1,str2) -> str:
#     inter = ''
#     id = 0
#     direct = 0  # 方向，1代表从左到右，0代表从右到左
#     if len(str1) > 1:
#         if len(str1) >= len(str2):#string1长度大于string2
#             if len(str2)>1:
#                 for i in range(len(str1)):
#                     inter += (str1[i] + str2[id])
#                     if i % (2*(len(str2) - 1)) < (len(str2) - 1) :#每经过str2长度-1，改变方向
#                         id += 1
#                     else:#str2从右到左，id+1
#                         id -= 1
#         elif len(str1) < len(str2):#string2长度大于string1
#             for i in range(len(str2)):
#                 inter += (str1[id] + str2[i])
#                 if i % (len(str1) - 1) == 0:
#                     if direct == 1:
#                         direct = 0
#                     else:
#                         direct = 1
#                 if direct == 1:
#                     id += 1
#                 else:
#                     id -= 1
#     else:
#         for i in range(len(str2)):
#             inter += (str1 + str2[i])
#     return inter

# print(loopy_madness('ab','12'))



str1 = ''#总字符
list3 = []#词汇本

#输入模块
# while 1:
#     x = input('输入句子，以#结尾结束输入:')
#     str1 +=x+' '
#     if x == '#':
#         break
#
# list2 = str1[:-2].split(' ')#分割出每一个单词
# for i in list2:
#     if i not in list3:#如果词汇本中不存在单词list[0]，则将list[0]加入词汇本
#         list3.append(i)
# list3.sort()#将词汇本排序
# j=1
# for i in list3[1:]:
#     print('NO'+str(j)+':'+i)
#     j+=1
# import lab8,csv
# from io import StringIO
# f = open('sample_data.csv')
# test = """4
# 2,3
# 2,2
# 3,2
# 4,3
# 2,2,3
# 3,2,4
# 4,2
# 1,2
# 2,2
# 3,2
# 4,2
# 1,2,3
# 4,5,6
# 7,8,9
# 22,33,44
#
# """
# final = [[[77, 99, 99, 48, 31],
#           [96, 63, 10, 36, 7],
#           [11, 66, 5, 72, 32],
#           [74, 99, 14, 5, 35]],
#          [[1, 37, 55, 33, 45, 98, 36],
#           [90, 1, 57, 95, 88, 56, 81],
#           [35, 11, 75, 11, 35, 38, 85],
#           [46, 3, 51, 49, 73, 17, 90],
#           [27, 99, 93, 58, 18, 30, 65],
#           [91, 59, 14, 15, 82, 72, 3]]]
# final2 = [[[2,2,3],
#            [3,2,4]],
#           [[4,2],
#            [1,2]],
#           [[2,2],
#            [3,2],
#            [4,2]],
#           [[1,2,3],
#            [4,5,6],
#            [7,8,9],
#            [22,33,44]]]
# print(type(f))
# # for row in f:
# #     print(row)
# # a = lab8.get_elevation_maps(f)
# # if a==final:
# #     print(1)
# # print(final)
# # print(lab8.get_elevation_maps(f))
# # f.close()
# # print(final2)
# # print(lab8.get_elevation_maps(StringIO(test)))
# lst4=[2,3,4]
# a=0
# for i in lst4:
#     i+=a
#     a=i
#     print(i)
import csv
def write_elevation_maps(maps_file,maps_list):
    file_header = [];
    file_content = [];
    map_count = len(maps_list);
    # 第一行的内容
    file_header.append([map_count])
    if (map_count > 0):
        # 二层循环-第一层
        for map_item in maps_list:
            # 获取header内容，是否有list为空的情况？为空则不写入
            if (len(map_item) > 0):
                file_header.append([len(map_item), len(map_item[0])])
                # 二层循环-第二层
                # print(map_item)
                for map_row in map_item:
                    file_content.append(map_row)
    row_lst = file_header+file_content
    print(row_lst)
    # 将row_lst写入map_file
    for i in row_lst:
        f_csv = csv.writer(maps_file)
        f_csv.writerow(i)
maps_list = [[[2,2,3],
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
f = open('test.csv','w')
print(write_elevation_maps(f, maps_list))
f.close()
# write_elevation_maps('test.csv',maps_list)
# list1=[]
# for i in list1:
#     print(123)
#[[4], [2, 3], [2, 2], [3, 2], [4, 3], [2, 2, 3], [3, 2, 4], [4, 2], [1, 2], [2, 2], [3, 2], [4, 2], [1, 2, 3], [4, 5, 6], [7, 8, 9], [22, 33, 44]]
#[[4], [2, 3], [2, 2], [3, 2], [4, 3], [2, 2, 3], [3, 2, 4], [4, 2], [1, 2], [2, 2], [3, 2], [4, 2], [1, 2, 3], [4, 5, 6], [7, 8, 9], [22, 33, 44]]
#['4', '2,3', '2,2', '3,2', '4,3', [2, 2, 3], [3, 2, 4], [4, 2], [1, 2], [2, 2], [3, 2], [4, 2], [1, 2, 3], [4, 5, 6], [7, 8, 9], [22, 33, 44]]
