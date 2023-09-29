# import random
# repeat = "3"
# while 1:
#     if repeat == "3":
#         global a,b,c,d,f
#         a = input("输入第一个选项：")
#         b = input("输入第二个选项：")
#         c = input("输入第三个选项：")
#         d = input("输入第四个选项：")
#         f = [a, b , c, d]
#         print("随机选择器，四选一（ 暂时只能做到这样，没反应就多试几次... ）")
#         print("电脑的决定是：" + random.choice(f))
#         repeat = input("输入1退出程序 \n输入2再次选择 \n输入3重新开始 \n请输入：")
#     elif repeat == "2":
#         print("电脑的决定是：" + random.choice(f))
#         repeat = input("输入1退出程序 \n输入2再次选择 \n输入3重新开始 \n请输入：")
#     elif repeat == "1":
#         print("结束")
#         break
#     # 有了下面这个代码后指令有点问题...
#     # 复现：电脑做完第一次决定后输入指令2 ，按预期运行。但再次输入2或3，没有给出重新判断的结果或再运行，输入1却可以正常结束。
#     # 下面代码预期的是：当没有出现指令数字时要用户再次输入
#     else:
#         print("输入错误！")
#         repeat = input("输入1退出程序 \n输入2再次选择 \n输入3重新开始 \n请输入：")
# exit(0)
# for i in range(4):
#     for j in range(i,-1,-1):
#         print(j,end='')
#     print('')
# for i in range(4,-1,-1):
#     for j in range(i,-1,-1):
#         print(j,end='')
#     print('')
# counter = 0
# for i in range(101,201):
#     for j in range(2,i):
#         if i%2!=0 :
#             print(i,'是质数')
#             counter+=1
#             break
#
# print(counter)