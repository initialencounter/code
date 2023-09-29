
# f_name = input('手机文件名：')
#
# os.system('./adb pull /storage/emulated/0/Download{} /Users/mac/PycharmProjects/pythonProject/'.format(f_name))
# f_name = f_name.replace('m3u8','txt')
#
# a = open('149790')
# b = a.read()
# c = b.replace('/data/user/0/com.ilulutv.fulao2/files/Fulao2','/storage/emulated/0/Download')
# f_name = f_name.replace('txt','m3u8')
#
# with open('f_name','w') as file_obj:
#     file_obj.write(c)
#     file_obj.close()
# os.system('./adb push /Users/mac/PycharmProjects/pythonProject/{} /storage/emulated/0/Download'.format(f_name))
import os
from Crypto.Cipher import AES
iv = b'0000000000000000'
name = input('文件名称：')
file_dir = '//Users/mac/PycharmProjects/pythonProject/{}/ts'.format(name)
file2 = '//Users/mac/PycharmProjects/pythonProject/{}'.format(name)
#读取密匙
key = open('//Users/mac/PycharmProjects/pythonProject/{}/php/key.php'.format(name))
key = key.read()
cipher = AES.new(key,AES.MODE_CBC,iv)
for w,e,f in os.walk(file_dir):#获取ts文件列表
    ffn = f[1][0:18]#获取ts文件头
    for i in range(0,372):
        ii = ffn+str(i)+'.ts'#加入序号
        print(ii)
        res = open('//Users/mac/PycharmProjects/pythonProject/{}/ts/{}'.format(name,ii),'rb')#打开ts文件
        res = res.read()#读取文件
        plain_data = cipher.decrypt(res)#解密
        with open('{}.ts'.format(name),'ab+') as w:
            w.write(plain_data)#写入视频
w.close()


