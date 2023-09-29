import os,re
from Crypto.Cipher import AES
list = []
iv = b'0000000000000000'
name = '147624'#input('文件名称：')
file_dir = '//Users/mac/PycharmProjects/pythonProject/{}/ts'.format(name)
file2 = '//Users/mac/PycharmProjects/pythonProject/{}'.format(name)
f = open(file2+'/'+name+'.m3u8')
ff= f.read()
match_key = re.findall('(?<={}).*?(?=\.php)'.format(name),ff)
key_url = name+match_key[0]+'.php'
key = open(key_url).read()
# match_iv = re.findall('(?<=IV=).*?(?=\s)',ff)[0][18:]
# print(match_iv)
# print(len(match_iv))
match_url = re.findall('(?<={}).*?(?=\.ts)'.format(name),ff)
print(match_url)
for i in match_url:
    ts_url = name+i+'.ts'
    list.append(ts_url)
# print(list)
cipher = AES.new(key,AES.MODE_CBC,iv)
for f in list:#获取ts文件列表
        res = open(f,'rb')#打开ts文件
        res = res.read()#读取文件
        plain_data = cipher.decrypt(res)#解密
        with open('{}1.ts'.format(name),'ab+') as w:
            w.write(plain_data)#写入视频
w.close()
#