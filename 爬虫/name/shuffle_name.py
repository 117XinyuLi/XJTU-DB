# 读入name.txt文件，打乱姓名顺序，重新写入shuffle_name.txt文件

import random

with open('name.txt', 'r', encoding='utf-8') as f:
    name_list = f.readlines()
    random.shuffle(name_list)
    with open('shuffle_name.txt', 'w', encoding='utf-8') as f:
        for name in name_list:
            f.write(name)
    print('打乱姓名顺序完成')
