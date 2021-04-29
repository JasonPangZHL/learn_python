from os import walk, mkdir, remove
import os
from shutil import copy, move

#桌面的数据整理 基于名字
path = 'file_prac' #os.walk 返回 文件路径 文件夹 文件
for filepath, folders, files in walk(path):
    # print(filepath, files,)
    for file in files:

        if 'docx' in file:
            print(os.path.join(filepath,file)) #r'c:\aa\aa.jpg'  'c:\\aa\\aa.jpg' /aaa/aa.jpg
            copy(os.path.join(filepath,file),os.path.join(r'backupfoldder\docx', file))
           #move
        elif 'ppt' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'backupfoldder\ppt', file))
           #move
        elif 'txt' in file:
            if os.path.exists(r'backupfoldder\txt'):

                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfoldder\txt', file))

            else:
                print('txt is not existed and create folder')
                os.mkdir(r'backupfoldder\txt')

                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backupfoldder\txt', file))

#压缩处理



import zipfile
def zipf():
    z = zipfile.ZipFile( 'abc.zip','w' )
    for file in os.listdir('zipfolder'):
        z.write(os.path.join('zipfolder',file))
        with open('abc.txt','a',encoding='gbk') as w: #注意编码问题
            w.write(file+'\n') #
    z.close()

# zipf()


def unzipf():
    f = zipfile.ZipFile('abc.zip', 'r')
    for file in f.namelist():
        f.extract(file, "MYunzip/")
unzipf()





