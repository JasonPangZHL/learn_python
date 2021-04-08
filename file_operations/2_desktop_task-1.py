from os import walk, mkdir, remove
import os
from shutil import copy, move

# 桌面的数据整理，基于名字
path = 'file_path'  # os.walk 返回 文件路径 文件夹 文件
for filepath, folders, files in walk(path):
    print(filepath, files,)
    for file in files:
        if '.docx' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'backup_folder\docx', file))
            move(os.path.join(filepath, file), os.path.join(r'backup_folder\docx', file))
        elif '.ppt' in file:
            print(os.path.join(filepath, file))
            copy(os.path.join(filepath, file), os.path.join(r'backup_folder\ppt', file))
            move(os.path.join(filepath, file), os.path.join(r'backup_folder\ppt', file))
        elif '.txt' in file:
            if os.path.exists(r'backup_folder\txt'):
                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backup_folder\txt', file))
                move(os.path.join(filepath, file), os.path.join(r'backup_folder\txt', file))
            else:
                print('txt is not existed and create folder')
                os.mkdir(r'backup_folder\txt')

                print(os.path.join(filepath, file))
                copy(os.path.join(filepath, file), os.path.join(r'backup_folder\txt', file))
                move(os.path.join(filepath, file), os.path.join(r'backup_folder\txt', file))
