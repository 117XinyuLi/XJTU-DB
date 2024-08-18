import requests
from lxml import etree
from selenium import webdriver
import time
import pandas as pd

detail_schools = ['北京大学', '清华大学', '复旦大学', '上海交通大学', '中国人民大学', '武汉大学', '中山大学',
                  '南京大学', '山东大学', '华中科技大学',
                  '西安交通大学', '四川大学', '东南大学', '中南大学', '哈尔滨工业大学', '北京航空航天大学', '同济大学',
                  '天津大学', '华南理工大学',
                  '北京师范大学', '东北大学', '大连理工大学', '华东师范大学', '吉林大学', '重庆大学', '西北工业大学',
                  '南开大学', '北京理工大学',
                  '兰州大学', '厦门大学', '湖南大学', '南京航空航天大学', '西南交通大学', '中国农业大学',
                  '北京交通大学', '中国矿业大学', '西北农林科技大学',
                  '中国海洋大学', '中国地质大学', '华中农业大学', '华东理工大学', '东北农业大学', '南京农业大学',
                  '中国药科大学', '南京理工大学',
                  '中国石油大学', '北京化工大学', '北京邮电大学', '北京林业大学', '北京中医药大学', '中国传媒大学',
                  '北京工商大学', '北京体育大学', '北京外国语大学', '中国音乐学院', '中央民族大学', '中国政法大学', '华北电力大学',
                    '华北理工大学', '南京艺术学院', '上海大学', '华东政法大学', '上海外国语大学', '上海财经大学', '上海师范大学']
for detail_school in detail_schools:

    # time.sleep(5)
    start = time.time()
    url = 'https://www.icourse163.org/university/view/all.htm#/'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.54'
    }
    r = requests.get(url).text
    tree = etree.HTML(r)
    # 获取大学链接
    href = tree.xpath('//a[@class="u-usity f-fl"]/@href')
    # 获取大学名称
    name = tree.xpath('//a[@class="u-usity f-fl"]/img/@alt')

    driver = webdriver.Edge()
    driver.maximize_window()


    def get_school_all_course():
        while (True):
            html = driver.page_source
            tree = etree.HTML(html)

            # 获取课程的链接
            hrefList = tree.xpath('//div[@class="um-spoc-course-list_wrap"]/div/a/@href')
            # 获取课程名称
            nameList = tree.xpath(
                '//div[@class="um-spoc-course-list_wrap"]/div/a/div[@class="u-courseCardWithTime-teacher"]/span/text()')
            # print(len(nameList))
            for x, y in zip(hrefList, nameList):
                x = 'https:' + x
                course_name.append(y)
                course_url.append(x)

            flag = (int(len(nameList)) != 20)

            if flag:
                break
            else:
                try:
                    # 点击下一页
                    a = driver.find_element_by_link_text('下一页')
                    a.click()
                    time.sleep(5)
                except:
                    return None
                get_school_all_course()


    def save(data, school):
        df = pd.DataFrame(data)
        df.to_csv('./{}.csv'.format(school), mode='a', encoding='ANSI', index=False, header=False)


    # 课程的链接
    course_url = []
    # 课程的名称
    course_name = []
    # time.sleep(5)
    for x, y in zip(href, name):
        school_link = 'https://www.icourse163.org' + x
        dict = {
            "大学名称": y,
            "大学课程链接": school_link
        }
        if dict["大学名称"] == detail_school:
            new_url = dict["大学课程链接"]
            driver.get(new_url)
            get_school_all_course()

            for i, j in zip(course_name, course_url):
                new_dict = {
                    "课程名称": [i],
                    "课程链接": [j]
                }
                save(new_dict, 'course')
            driver.close()
            end = time.time()
            print(detail_school, '慕课的所有课程保存完成')
            deltatime = end - start
            print("项目所用时间为:", deltatime)
