import random
import time
from os import system as sys
# class Lst_Error(Exception):
#     def __init__(self):
#         Exception.__init__(self)
#     def __str__(self):
#         return 'lst错误，无法被还原！'
# class Klt159:
#     yx = []
#     def __init__(self,lst1):
#         self.lst1 = lst1
#         self.lst2 = [[1,2,3,4],
#                     [5,6,7,8],
#                     [9,10,11,12],
#                     [13,14,15,16]]
#         self.dic = {'up':[-1,0],'down':[1,0],'right':[0,1],'left':[0,-1]}
#         self.lst_direction = []
#     def move1(self):
#         for i in range(4):
#             for j in range(4):
#                 if 16 == self.lst2[i][j]:
#                     Klt159.yx = [i,j]
#         print(Klt159.yx)
#     def move3(self):
#         print(Klt159.yx)
#         # pass
# a = Klt159([1]).move1()
# Klt159([1]).move3()
# print(Klt159.yx)
# class Salary:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     # @property
#     def getsalery_(self):
#         print(self.name)
#     # @getsalery.setter
#     # def getsalery(self,name):
#     #     self.__name = name
# def get(s):
#     print(123,s)
# Salary.getsalery_=get;
# s = Salary('xx',20)
# s.getsalery_()
# import copy
# class Person:
#     def __init__(self,name):
#         self.name = name
#         # self.__age = age
#     # @property
#     # def say_age(self):
#     #     print('{0}的年龄为{1}'.format(self.name,self.__age))
#     def __add__(self, other):
#         if isinstance(other,Person):
#             return '{0}--{1}'.format(self.name,other.name)
#         else:
#             return '不能'
#     def __mul__(self, other):
#         if isinstance(other,int):
#             return '{0}'.format(self.name*other)
#         else:
#             return '不能'
# # class Zw(Person):
#     def __init__(self,name,age):
#         Person.__init__(self,name,age)
#
# zw = Zw('zw',21)
# zw.say_age
# print(zw._Person__age)
# class Cpu:
#     def ca(self):
#         print('ca')
# class Screen:
#     def show(self):
#         print('sh')
# class Iph:
#     def __init__(self,cpu,screen):
#         self.cpu = cpu
#         self.screen = screen
# cp = Cpu()
# scr = Screen()
# ip = Iph(Cpu(),Screen())
# ip.cpu.ca()
class Car_factory:
    __obj = None
    __init_flag = True
    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__(cls)
        return cls.__obj
    def __init__(self):
        if Car_factory.__init_flag == True:
            print('122312')
            Car_factory.__init_flag = False
    def car_brand(self,brand):
        if brand == '奔驰':
            return Benz()
        elif brand == '宝马':
            return BMW()
        elif brand == '比亚迪':
            return BYD()
        else:
            return 'false'

class Benz:
    pass
class BMW:
    pass
class BYD:
    pass

car_factory = Car_factory()
print(car_factory.car_brand('宝马'))
car_factory2 = Car_factory()
print(car_factory,car_factory2)
# class Car_factory:
#     __obj = None
#     __init_flag = True
#     def __new__(cls, *args, **kwargs):
#         if not cls.__obj:
#             cls.__obj = object.__new__(cls)
#         return cls.__obj
#     def __init__(self):
#         # print('12')
#         if Car_factory.__init_flag == True:
#             print('122312')
#             Car_factory.__init_flag = False
# c1 = Car_factory()
# c2 = Car_factory()
# print(c1,c2)
# # 实例化一个单例
# class Singleton(object):
#     __instance = None
#
#     def __new__(cls, age, name):
#         #如果类数字__instance没有或者没有赋值
#         #那么就创建一个对象，并且赋值为这个对象的引用，保证下次调用这个方法时
#         #能够知道之前已经创建过对象了，这样就保证了只有1个对象
#         if not cls.__instance:
#             cls.__instance = object.__new__(cls)
#         return cls.__instance
#
# a = Singleton(18, "xxx")
# b = Singleton(8, "xxx")
#
# print(id(a))
# print(id(b))
#
# a.age = 19 #给a指向的对象添加一个属性
# print(b.age)#获取b指向的对象的age属性