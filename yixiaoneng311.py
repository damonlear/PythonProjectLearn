import requests
import os
from bs4 import BeautifulSoup
import time
import datetime

# 打包程序
# conda activate py38
# D:\workspace\pythonProjectLearn>pyinstaller
# pyinstaller -F yixiaoneng311.py

start_311_date = '2022-08-15'
date_format_default = '%Y-%m-%d'
date_format_1 = '%Y.%m.%d'
date_format_2 = '%Y年%m月%d日'


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

# url是带占位符{},使用时需格式化,填入日期yyyy-MM-dd
group_url = {'A组': a_url,
             'B组': b_url,
             'C组': c_url,
             'D组': d_url,
             'F组': f_url,
             'G组': g_url,
             'I组': i_url,
             'X组': x_url
             }
group_count = {'A组': 1,
               'B组': 2,
               'C组': 3,
               'D组': 4,
               'F组': 5,
               'G组': 6,
               'I组': 7
             }


def readSouceGroup():
    fileName = '311.name'
    while(True):
        if os.path.exists(fileName):
            break
        else:
            print("班级名单文件{}不存在，请复制名单到根目录".format(fileName))
            time.sleep(1)

    arrays = []
    with open(fileName, 'r', encoding='utf-8') as f:
        for line in f:
            # print(line)
            line = line.rstrip()
            if (line != ''):
                arrays.append(line)
    return arrays

# 网络上实际的签到人数
def requestQiandao(url):
    # 密码311
    cookies = {"rs_token_C4ypA4": "311"}
    page = requests.get(url
                        , cookies=cookies
                        )
    # print(page.text)

    page.encoding = "utf-8"
    # 网页格式化
    soup = BeautifulSoup(page.text, features="html.parser")
    # 学员名字 找td标签属性为name-field的内容
    name_items = soup.find_all("td", class_="name-field")
    # 学员学号
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

        array.append(i + n)
    array.sort()
    return array


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
    print("--------------------------------------------")
    print("易效能311期打卡委员统计脚本(内测版)")
    print("易效能311期打卡委员统计脚本(内测版)")
    print("易效能311期打卡委员统计脚本(内测版)")
    print("--------------------------------------------")
    print("开发者说明")
    print("开发者说明")
    print("developer : Damon Lee Code in 2022-09-28 Version 1.0")
    print("developer : Damon Lee Code in 2022-09-28 Version 1.0")
    print("从网络查询易效能签到网站查询出对应日期的各组签到情况，从全员名单文件name.txt文件中剔除，剩余的就为当天未签到的人员名单")
    print("签到名单311.name改变时，可能导致统计不正确")
    print("--------------------------------------------")
    print("支持说明")
    print("支持说明")
    print("仅支持容效能311期签到查询")
    print("仅支持Windows电脑系统使用")
    print("--------------------------------------------")
    print("--------------------------------------------")

def getlocalStrTime(formate = date_format_default):
    times = time.time()
    local_time = time.localtime(times)
    local_strftime = time.strftime(formate, local_time)
    print("今天日期：{}".format(local_strftime))
    return local_strftime

def formateStrTime(source_time, source_formate_0, target_formate_1):
    a = datetime.datetime.strptime(source_time, source_formate_0)
    b = datetime.datetime.strftime(a, target_formate_1)
    return b

def getInputTime():
    while (True):
        try:
            print("请输入要查询统计的日期，输入格式为yyyy-MM-dd[{}]，点击Enter默认输入为今天".format(getlocalStrTime()))
            print('例如:2021-01-01')
            print('点击Enter默认输入为今天')
            inputyyyyMMdd = input()
            if inputyyyyMMdd == '':
                inputyyyyMMdd = getlocalStrTime()
            else:
                time.strptime(inputyyyyMMdd, "%Y-%m-%d")
            return inputyyyyMMdd
            pass
        except Exception as e:
            print("请输入日期格式异常，格式为yyyy-MM-dd\r\n{}".format(e))
            pass

# 判断中文
def is_Chinese(ch):
    if '\u4e00' <= ch <= '\u9fff':
        return True
    return False

# 名字只能是中文
def getLinkSampleStr(str_a, str_b):
    linkSampleStrArrays = []
    for i_index_b in range(len(str_b)):
        # 找str_b[i]在不在str_a里面
        # print("找数字：{}-{}".format(str_a.find(str_b[i]), str_b[i]))
        start_a_index = str_a.find(str_b[i_index_b])
        if start_a_index == -1:
            # 找str_b[i]不在str_a里面，直接继续找
            continue
        elif is_Chinese(str_b[i_index_b]) == False:
            continue
        else:
            # print("position A={} B={}".format(start_a_index, i_index_b))
            lastStr = ''
            for i_find_b in range(i_index_b, len(str_b) + 1):
                # print('find in range 从{}到{} = {}'.format(i_index_b, i_find_b, str_b[i_index_b: i_find_b]))
                if str_a.find(str_b[i_index_b: i_find_b]) == -1:
                    break
                else:
                    lastStr = str_b[i_index_b: i_find_b]
                    continue
            if len(lastStr) > 1:
                linkSampleStrArrays.append(lastStr)
    if len(linkSampleStrArrays) == 0:
        return ''
    else:
        linkSampleStrArrays.sort()
        return linkSampleStrArrays[0]

def getDateTimeSjc(yyyyMMdd):
    time_1_struct = time.strptime(start_311_date, "%Y-%m-%d")
    time_2_struct = time.strptime(yyyyMMdd, "%Y-%m-%d")
    return time_2_struct.tm_yday - time_1_struct.tm_yday + 1

def getWeChatMessage(yyyyMMdd, a, b, c, d, f, g, i):
    fileName = 'wechat.message'
    while(True):
        if os.path.exists(fileName):
            break
        else:
            print("微信原始文件{}不存在，请复制文件到根目录".format(fileName))
            time.sleep(1)

    wechat_formate = open(fileName, 'r', encoding='utf-8').read()
    wechat = wechat_formate.format(formateStrTime(yyyyMMdd, date_format_default, date_format_1), getDateTimeSjc(yyyyMMdd),
                  formateStrTime(yyyyMMdd, date_format_default, date_format_2), getDateTimeSjc(yyyyMMdd),
                  a + b + c + d + f + g + i,
                  a, b, c, d, f, g, i)
    # print(wechat)
    return wechat

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    init()
    # 获取输入的日期
    yyyyMMdd = getInputTime()
    # 初始化文件
    os.mkdir(yyyyMMdd)
    fTotal = open('{}/{}简单统计.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')
    fno = open('{}/{}未打卡人员名单.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')
    fWechat = open('{}/{}发微信信息.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')

    # 读取本地名单
    arraysAll = readSouceGroup()
    # 遍历每组对应的查询今日签到的URL
    for group_name, group_url in group_url.items():
        realUrl = group_url.format(yyyyMMdd)
        # 统计组group_name来自网络打卡人员的集合
        tmpGroup = requestQiandao(realUrl)
        # 统计取这组的人数，目前写死
        tmpAll = getGroupPeopleCount(realUrl, yyyyMMdd)
        print('--------------------------------------------')
        print("网上签到情况={}".format(tmpGroup))
        print('签到情况统计=[{}][实到:{}][应到:{}]'.format(group_name, len(tmpGroup), tmpAll))

        fTotal.write("{}：实到{}，应到{}".format(group_name, len(tmpGroup), tmpAll) + os.linesep)
        # 统计用
        group_count[group_name] = len(tmpGroup)

        if len(tmpGroup) != tmpAll:
            print("-->【签到异常】{}应到{}实到{}".format(group_name, len(tmpGroup), tmpAll))
        for i in tmpGroup:
            for j in arraysAll:
                if getLinkSampleStr(i, j) != '':
                    # print('[原始数据={}][实际数据={}]'.format(i, j))
                    arraysAll.remove(j)
                    break

    print('--------------------------------------------')
    print("未签到：{}".format(arraysAll))
    print('--------------------------------------------')

    # os.linesep代表当前操作系统上的换行符
    fno.write('未签到名单' + "\n")
    for no in arraysAll:
        fno.write(no + "\n")

    fWechat.write(getWeChatMessage(yyyyMMdd,
                     group_count['A组'],
                     group_count['B组'],
                     group_count['C组'],
                     group_count['D组'],
                     group_count['F组'],
                     group_count['G组'],
                     group_count['I组']))

    fTotal.close()
    fno.close()
    fWechat.close()

    os.system("notepad {} ".format(fWechat.name))
    os.system("notepad {} ".format(fno.name))
    print("执行结束")
    print("文件保存在根目录")
    os.system("pause")


