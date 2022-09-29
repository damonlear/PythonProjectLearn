import requests
import os
import logging
from bs4 import BeautifulSoup
import time

a_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=7tVK&embedded='
b_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=H4wr&embedded='
c_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=4MXn&embedded='
d_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=8DzN&embedded='
e_url = ''
f_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=ZqNR&embedded='
g_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=Rzry&embedded='
h_url = ''
i_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=R1H6&embedded='
x_url = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D={}&q%5B0%5D%5Bfield_2_associated_field_3%5D=rZLB&embedded='
x_url_eg = 'https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D=2022-09-28&q%5B0%5D%5Bfield_2_associated_field_3%5D=rZLB&embedded='

group_url = {'A组': a_url,
             'B组': b_url,
             'C组': c_url,
             'D组': d_url,
             'F组': f_url,
             'G组': g_url,
             'I组': i_url,
             'X组': x_url
             }

def readSouceGroup():
    arrays = []
    with open('311.name', 'r', encoding='utf-8') as f:
        line = f.readline()
        while line:
            print(line)
            line = f.readline()
            if (line != ''):
                arrays.append(line)
    return arrays


def requestQiandao(url):
    # 密码311
    cookies = {"rs_token_C4ypA4": "311"}
    page = requests.get(url
                        , cookies=cookies
                        )
    # print(page.text)

    page.encoding = "utf-8"
    soup = BeautifulSoup(page.text, features="html.parser")
    name_items = soup.find_all("td", class_="name-field")
    id_items = soup.find_all("td", class_="cascade-drop-down")
    array = []
    # for company_item in name_items:
    # dd = company_item.text.strip()
    # print(company_item)
    # print(dd)
    # array.append(dd)

    for index in range(len(name_items)):
        n = name_items[index].text.strip()
        i = id_items[index].text.strip()

        # print(n)
        # print(i)
        array.append(i + n)
    array.sort()
    return array


def getUrlArrays(yyyy_MM_dd):
    urlArrays = []
    urlArrays.append(a_url.format(yyyy_MM_dd))
    urlArrays.append(b_url.format(yyyy_MM_dd))
    urlArrays.append(c_url.format(yyyy_MM_dd))
    urlArrays.append(d_url.format(yyyy_MM_dd))
    urlArrays.append(f_url.format(yyyy_MM_dd))
    urlArrays.append(g_url.format(yyyy_MM_dd))
    urlArrays.append(i_url.format(yyyy_MM_dd))
    urlArrays.append(x_url.format(yyyy_MM_dd))
    return urlArrays


def getGroupPeopleCount(url, yyyyMMdd):
    if url == a_url.format(yyyyMMdd):
        return 11
    elif url == b_url.format(yyyyMMdd):
        return 12
    elif url == c_url.format(yyyyMMdd):
        return 10
    elif url == d_url.format(yyyyMMdd):
        return 11
    elif url == f_url.format(yyyyMMdd):
        return 11
    elif url == g_url.format(yyyyMMdd):
        return 11
    elif url == i_url.format(yyyyMMdd):
        return 7
    elif url == x_url.format(yyyyMMdd):
        return 16
    else:
        return 0


def find_repeat(source, elmt):  # The source may be a list or string.
    elmt_index = []
    s_index = 0
    e_index = len(source)

    while (s_index < e_index):
        try:
            temp = source.index(elmt, s_index, e_index)
            elmt_index.append(temp)
            s_index = temp + 1
        except ValueError:
            break
    return elmt_index

def init():
    log = logging.getLogger()
    log.setLevel("ERROR")

def getlocalStrTime():
    times = time.time()
    local_time = time.localtime(times)
    local_strftime = time.strftime("%Y-%m-%d", local_time)
    print("今天日期：{}".format(local_strftime))
    return local_strftime


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    print("请输入要查询统计的日期，格式为yyyy-MM-dd[{}]，默认为今天".format(getlocalStrTime()))
    yyyyMMdd = input()
    if yyyyMMdd == '':
        yyyyMMdd = getlocalStrTime()

    arraysAll = readSouceGroup()

    # for thisUrl in getUrlArrays(yyyyMMdd):
    # tmpGroup = requestQiandao(thisUrl)
    # print(tmpGroup)

    tmpUrlArrays = getUrlArrays(yyyyMMdd)
    for index in range(len(tmpUrlArrays)):
        tmpGroup = requestQiandao(tmpUrlArrays[index])
        tmpAll = getGroupPeopleCount(tmpUrlArrays[index], yyyyMMdd)
        print(tmpGroup)
        print('应到{} 实到{}'.format(tmpAll, len(tmpGroup)))

    iii = find_repeat('G组 - 01郑宝娟', 'G01 郑宝娟')
    print("找相同元素：{}".format(iii))
