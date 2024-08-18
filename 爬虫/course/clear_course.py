# 读取course.csv文件，将所有课程保存在clear_course.txt文件中，去除重复的课程。

import pandas as pd

# 没有表头
df = pd.read_csv('course.csv', header=None, encoding='ANSI')
# 取出第一列
df = df.iloc[:, 0]
# 去重
df = df.drop_duplicates()
# 保存
df.to_csv('clear_course.txt', index=False, header=False, encoding='utf-8')

