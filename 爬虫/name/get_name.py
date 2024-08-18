# 从https://www.resgain.net/name_list.rhtml?fid=i i是一个整数，爬取7000个姓名

import requests
from bs4 import BeautifulSoup
import re
import time
import random
import os


def get_name():
    total_name = 7000
    url = 'https://www.resgain.net/name_list.rhtml?fid='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    for i in range(1, 500):
        try:
            response = requests.get(url + str(i), headers=headers)
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            name_list = soup.find_all('div', class_='cname')[0:int(total_name//500+1)]
            for name in name_list:
                name = name.get_text()
                name = re.sub(r'\s+', '', name)
                with open('name.txt', 'a', encoding='utf-8') as f:
                    f.write(name + '\n')
            print('已爬取第{}页'.format(i))
            time.sleep(random.randint(1, 3))
        except Exception as e:
            print(e)
            continue
    print('爬取完成')


if __name__ == '__main__':
    get_name()

