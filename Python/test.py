import os
ts_video_dir="/storage/emulated/0/Android/data/com.example.astarte/files/video/"
def hebing(name):

    file_dir = ts_video_dir+name
    filelist=os.listdir(file_dir)
    filelist.sort()
    print(filelist)
    if 'index.m3u8' not in os.listdir(file_dir):
         return
    for f in os.listdir(file_dir):#获取ts文件列表
        if f[-2:]!='ts':
             break
        print(f)
        

for i in os.listdir(ts_video_dir):
    print(i)
    if i!='.DS_Store':
        hebing(i)