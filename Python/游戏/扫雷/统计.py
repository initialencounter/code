import os,re
lst = os.listdir('/Users/mac/Desktop/Arbiter_0.52.3')
lst_all = []
lst_beg = []
lst_int = []
lst_exp = []
dic_={}
for i in lst:
    if i[-4:]=='.avf':
        if i[0]!='H':
            if i[0]=='I':
                lst_int.append(i)
            if i[0]=='B':
                lst_beg.append(i)
            if i[0] == 'E':
                lst_exp.append(i)
class avf():
    def __init__(self,name):
        self.bvs = name[-18:-14]
        self.time = name.split('_')[1]
        self.bv = name.split('_')[2][4:]
def print_lst(lst1):
    count = 0
    for i in lst1:
        af = avf(i)
        if (i[0]=='B' and int(af.bv)>=10) or (i[0]=='I' and int(af.bv)>=30) or (i[0]=='E' and int(af.bv)>100):
            count += 1
            dic_[i]=float(af.time)
            print(af.time,af.bvs,end=' | ')
            if count%6==0:
                print()
    print()
print('初级局数：'+str(len(lst_beg)))
print_lst(lst_beg)
print('中级局数：'+str(len(lst_int)))
print_lst(lst_int)
print('高级局数：'+str(len(lst_exp)))
print_lst(lst_exp)
print(dic_)
x = sorted(dic_.items(),key=lambda x:x[1])
for i in x:
    print(i)