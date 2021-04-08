import os
# from shutil import copy, move

# 基础文件获取
path = 'file_path'  # os.walk 返回 文件路径 文件夹 文件
# 输出当前目录所有内容，有文件夹会穿透进去
for filepath, folders, files in os.walk(path):
    # print(filepath, folders, files)
    for file in files:
        print(os.path.join(filepath, file))
        # print(file)

# 输出当前目录内容，不会穿透
for file in os.listdir(path):
    # print(file)
    if 'txt' in file:
        print(file)
