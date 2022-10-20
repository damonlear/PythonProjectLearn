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

x_url = 'https://www.makio.it/pokemon/sv-dex/'
x_attribute_url = 'https://www.makio.it/pokemon/'

class Pokemon:

    def __init__(self, number, name, image, attribute: list):
        self.number = number
        self.name = name
        self.image = image
        self.attribute = attribute

    def __repr__(self):
        return repr((self.number, self.name, self.image, self.attribute))

# 核心代码
# 有三种类型
def requestQiandao(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'}

    page = requests.get(url=url, headers=headers)
    # print(page.text)
    page.encoding = "utf-8"
    # 网页格式化
    soup = BeautifulSoup(page.text, features="html.parser")
    # 网页有多个部分，只抓取pokedex部分
    pokedex = soup.find('div', class_='pokedex')
    # 实际的网页里一个大的个子可能包含一个或多个宝可梦
    tables = pokedex.find_all('div', {"data-aos": "fade-up"})
    print("抓包 tables ： {}".format(len(tables)))
    array = []
    if tables == None:
        return array

    for table in tables:
        # 内部列表，可能是一个，也可能是多个，标题头部的模块
        inner_tables = table.find_all('div', {'data-aos': 'zoom-in'})
        print("抓包 inner_tables ： {}".format(inner_tables))
        if (inner_tables == None):
            continue
        for inner_table in inner_tables:
            pokemon_number = inner_table.find('h4')
            pokemon_name = inner_table.find('h3')
            pokemon_image_paser = inner_table.find('img', class_='image imageBig')
            pokemon_image = ''
            if(pokemon_image_paser == None):
                pokemon_image_paser = inner_table.find('img', class_='image imageBig newsPulse')
                if (pokemon_image_paser == None):
                    pokemon_image = '#'
                else:
                    pokemon_image = formate_img_url(x_url, pokemon_image_paser['src'])
            else:
                pokemon_image = formate_img_url(x_url, pokemon_image_paser['src'])
            # 保存对象
            inner_pokemon = Pokemon(
                pokemon_number.text,
                pokemon_name.text,
                pokemon_image,
                [])
            pokemon_attributes = inner_table.find('div', class_='typeDivReal').find_all('img', class_='typeBig')
            for pokemon_attribute in pokemon_attributes:
                print('图片：', pokemon_attribute['src'])
                print('图片格式化：', formate_img_url(x_attribute_url, pokemon_attribute['src']))
                inner_pokemon.attribute.append(formate_img_url(x_attribute_url, pokemon_attribute['src']))
            array.append(inner_pokemon)
            # print(inner_pokemon)
    return array

def formate_img_url(baseUrl, img_url):
    if(img_url.startswith('../')):
        return img_url.replace('../', baseUrl).replace(' ', '%20')
    elif(img_url.startswith('http')):
        return img_url.replace(' ', '%20')
    else:
        return (baseUrl + img_url).replace(' ', '%20')


def init():
    print("--------------------------------------------")
    print("宝可梦朱紫抓包")
    print("抓包https://www.makio.it/pokemon/sv-dex/")
    print("统计脚本(内测版)")
    print("统计脚本(内测版)")
    print("统计脚本(内测版)")
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    pokemon_file = open('pokemon_leaks.csv', 'w+', encoding='utf-8')
    array_all = []
    print("请求{}".format(x_url))
    # 核心代码：爬虫核心 一切数据的基数
    tmpGroup = requestQiandao(x_url)
    array_all.extend(tmpGroup)
    print('--------------------------------------------')
    print('准备排序--------------------------------------------')
    # array_all.sort(key=lambda x: x.metascore_w, reverse=True)
    print('准备排序结束--------------------------------------------')
    for p in array_all:
        print("写文件", p)
        line = p.name + ' ,' + p.image + ' ,' + ' ,' + p.number + ' ,'
        for pi in p.attribute:
            line += "<img src='{}'>".format(pi)
        line += '\n'
        pokemon_file.write(line)

    print('--------------------------------------------')
    print('-->')
    print('-->')
    print('--------------------------------------------')
    pokemon_file.close()
    os.system("pause")
