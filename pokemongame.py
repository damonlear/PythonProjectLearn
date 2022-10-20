import requests
import os
from bs4 import BeautifulSoup
import time
import datetime
import functools
import re

# 打包程序
# conda activate py38
# D:\workspace\pythonProjectLearn>pyinstaller
# pyinstaller -F yixiaoneng311.py

x_url = 'https://www.metacritic.com/search/game/pokemon/results?page={}'
x_url_eg = 'https://www.metacritic.com/search/game/pokemon/results?page=0'

# 用于输出统计完成
group_out_finish = []


class Pokemon:
    metascore_w = -1

    def __init__(self, title, platform, year, metascore_w, deck, src):
        self.title = title
        self.platform = platform
        self.year = year
        self.metascore_w = metascore_w
        self.deck = deck
        self.src = src

    def __repr__(self):
        return repr((self.title, self.platform, self.year, self.metascore_w, self.deck, self.src))


# 核心代码
def requestQiandao(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    page = requests.get(url=url, headers=headers)
    # print(page.text)
    page.encoding = "utf-8"
    # 网页格式化
    soup = BeautifulSoup(page.text, features="html.parser")
    tables = soup.find_all('div', class_='result_wrap')
    array = []
    if tables == None:
        return array

    # 名字
    title = ''
    # 平台
    platform = ''
    # 发行年
    year = ''
    # 分数
    metascore_w = 0
    # 描述
    deck = ''
    # 图片
    src = '#'

    for table in tables:
        # 标题头部的模块
        top_div = table.find('div', class_='main_stats')
        if (top_div == None):
            return array

        # 名字
        title = top_div.find('h3', class_='product_title basic_stat').find('a').text.strip()
        # 平台
        platform = top_div.find('span', class_='platform').text.strip()
        # 发行年
        source_year = top_div.find('p').text.strip()
        if (re.search(r"(\d{4})", source_year) == None):
            year = ''
        else:
            year = re.search(r"(\d{4})", source_year).group(0)

        # 分数
        a = top_div.find('span', class_='metascore_w medium game positive')
        if (a == None):
            a = table.find('span', class_='metascore_w medium game mixed')
        if (a == None):
            a = table.find('span', class_='metascore_w medium game tbd')
            if (a == 'tbd'):
                metascore_w = 0
        if (a == None):
            metascore_w = 0
        else:
            if (a.text.strip().isdigit() == False):
                metascore_w = 0
            else:
                metascore_w = int(a.text.strip())

        # 描述
        source_deck = table.find('p', class_='deck basic_stat')
        if (source_deck == None):
            deck = ''
        else:
            deck = source_deck.text.strip()
        # 图片
        src = table.find('div', class_='result_thumbnail').find('img')['src']

        array.append(Pokemon(title, platform, year, metascore_w, deck, src))

    # array.sort(key=lambda x:x.metascore_w)
    return array


def init():
    print("--------------------------------------------")
    print("(内测版)")
    print("(内测版)")
    print("(内测版)")
    print("--------------------------------------------")
    print("开发者说明")
    print("开发者说明")
    print("developer : Damon Lee Code in 2022-09-28 Version 1.0")
    print("developer : Damon Lee Code in 2022-09-28 Version 1.0")
    print("--------------------------------------------")
    print("支持说明")
    print("支持说明")
    print("仅支持Windows电脑系统使用")
    print("--------------------------------------------")
    print("--------------------------------------------")
    group_out_finish.clear()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    pokemon_file = open('pokemon.csv', 'w+', encoding='utf-8')
    array_all = []

    for x in range(22):
        time.sleep(1)
        realUrl = x_url.format(x)
        print("请求{}".format(realUrl))
        # 核心代码：爬虫核心 一切数据的基数
        tmpGroup = requestQiandao(realUrl)
        array_all.extend(tmpGroup)

        print('--------------------------------------------')
        # print("网上签到情况={}".format(tmpGroup))

    print('准备排序--------------------------------------------')
    array_all.sort(key=lambda x: x.metascore_w, reverse=True)
    print('准备排序结束--------------------------------------------')
    for p in array_all:
        print(p)
        pokemon_file.write(
            p.title.replace(',', ' ') + ' , ' + p.src + ' , ' + ' , ' + re.sub(r'[\s]+', ' ', p.deck).replace(',',
                                                                                                              ' ') + ' , ' + p.platform + ' , ' + str(
                p.year) + ' , ' + str(p.metascore_w) + '\n')

    print('--------------------------------------------')
    print('-->')
    print('-->')
    print('--------------------------------------------')
    pokemon_file.close()
    os.system("pause")
