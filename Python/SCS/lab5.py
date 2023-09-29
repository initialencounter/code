def sum_string(str_)-> int:

    sum = 0
    if str_ ==None:
        return sum
    for i in range(len(str_)):
        if int(i) % 2 == 0:
            sum += int(str_[i])
        else:
            sum -= int(str_[i])
    return sum


# def substring_with_largest_sum_(str_) -> str:
#     if str_ == '':
#         return ''
#     largest = 0
#     for step in range(len(str_)):
#         if str_[0] == '0':
#             step = len(str_) - step
#         id = 0
#         for j in range(len(str_)):
#             if id + step > len(str_):
#                 continue
#             j = str_[id:id + step]
#             k = sum_string(j)
#             if k > largest:
#                 largest = k
#                 largest_str = j
#             id += 1
#     return largest_str
def substring_with_largest_sum(s) -> str:
    largest = 0
    if s =='':
        return ''
    for i in range(len(s)):
        for j in range(len(s[i:])):
            j = s[i:][:j+1]
            k = sum_string(j)
            if k > largest:
                largest = k
                largest_str = j
    return largest_str
def loopy_madness2(str1,str2) -> str:
    inter = ''
    id = 0
    direct = 0  # 方向，1代表从左到右，0代表从右到左
    if len(str1) > 1:
        if len(str1) >= len(str2):#string1长度大于string2
            for i in range(len(str1)):
                inter += (str1[i] + str2[id])
                if i % (len(str2) - 1) == 0:#每经过str2长度-1，改变方向
                    if direct == 1:
                        direct = 0
                    else:
                        direct = 1
                if direct == 1:#1str2从左到右，id-1
                    id += 1
                else:#str2从右到左，id+1
                    id -= 1
        elif len(str1) < len(str2):#string2长度大于string1
            for i in range(len(str2)):
                inter += (str1[id] + str2[i])
                if i % (len(str1) - 1) == 0:
                    if direct == 1:
                        direct = 0
                    else:
                        direct = 1
                if direct == 1:
                    id += 1
                else:
                    id -= 1
    else:
        for i in range(len(str2)):
            inter += (str1 + str2[i])
    return inter

#
def loopy_madness(str1,str2):
    inter = ''
    if len(str1) <= len(str2):
        str3 = str1[::-1][1:]
        str4 = str1[1:]
        for i in str2:
            str1 += str3 + str4
            if len(str1)>len(str2) or len(str1)==1:
                str1 = str1 * len(str2)
                break
        for i in range(len(str2)):
            inter += str1[i]+str2[i]
    elif len(str1) > len(str2):
        str3 = str2[::-1][1:]
        str4 = str2[1:]
        print(str3,str4)
        for i in str1:
            str2 += str3 + str4
            if len(str2)>len(str1) or len(str2)==1:
                str2=str2*len(str1)
                break
        for i in range(len(str1)):
            inter += str1[i]+str2[i]
    return inter
print(loopy_madness('a','cd'))