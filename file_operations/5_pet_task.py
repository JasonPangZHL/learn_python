from os import walk, mkdir, rename
import os
# from shutil import copy, move

# 以文件夹的名字给宠物命名
path = 'pets'  # os.walk 返回 文件路径 文件夹 文件
for filepath, folders, files in walk(path):
    print(filepath, folders, files)
    # 注意我们需要以文件夹名字 作为 文件夹下文件的名字，同时加上一个顺序
    counter = 0
    for file in files:
        print(filepath)
        type_name = filepath.split('\\')[-1]  # 注意使用这种方式取 文件夹的名字split
        renamed = type_name + str(counter) + '.jpg'  # 组合新名字
        # 注意这里为全路径 源文件 目标文件
        rename(os.path.join(filepath, file), os.path.join(filepath, renamed))
        counter += 1
