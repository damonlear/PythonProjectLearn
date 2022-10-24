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
groups_url = {'A组': a_url,
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
# 用于输出统计完成
group_out_finish = []

import smtplib
from email.mime.text import MIMEText
#设置服务器所需信息
#163邮箱服务器地址
mail_host = 'smtp.####.com'
#163用户名
mail_user = '####@####.com'
#密码(部分邮箱为授权码)
mail_pass = '####'
#邮件发送方邮箱地址
sender = '####@####.com'
#邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
receivers = ['####@####.com']

def sendEmail(content):
    # 设置email信息
    # 邮件内容设置
    message = MIMEText(content, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'title'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]
    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('发送成功')
    except smtplib.SMTPException as e:
        print('发送失败', e)  # 打印错误

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
def sendEmailFile(title, content, *files):
    # 创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = Header(receivers[0], 'utf-8')
    message['Subject'] = Header(title, 'utf-8')

    # 邮件正文内容
    message.attach(MIMEText(content, 'plain', 'utf-8'))

    for f in files:
        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(f, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="{}"'.format(f)
        message.attach(att1)

    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, 25)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print("SUCCESS: 邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

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

# 核心代码
# 网络上实际的签到人数
# 参考https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4?q%5B0%5D%5Bfield_1%5D=2022-09-30&q%5B0%5D%5Bfield_2_associated_field_3%5D=rZLB&embedded=
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

    if len(array) == 0:
        for one in requestOnlyOneQiandao(url):
            array.append(one)
    array.sort()
    return array

# 只有一个人时，整个页面就变了
# 参考https://edu2.yixiaoneng.com/f/fwzCUQ/s/C4ypA4/e/u5P9BO23?q%5B0%5D%5Bfield_1%5D=2022-09-30&q%5B0%5D%5Bfield_2_associated_field_3%5D=rZLB
def requestOnlyOneQiandao(url):
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
    name_items = soup.find_all("span", {"data-display-field-type":"name-field"})
    # 学员学号
    id_items = soup.find_all("span", {"data-display-field-type":"cascade-drop-down"})
    array = []

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
        return 9
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
    group_out_finish.clear()

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
def getYi():
    init()
    # 获取输入的日期
    yyyyMMdd = getlocalStrTime()
    # 初始化文件夹
    if not os.path.isdir(yyyyMMdd):
        os.mkdir(yyyyMMdd)
    # 输出文件的数据流
    fTotal = open('{}/{}简单统计.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')
    fno = open('{}/{}未打卡人员名单.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')
    fWechat = open('{}/{}发微信信息.txt'.format(yyyyMMdd, yyyyMMdd), 'w+', encoding='utf-8')

    # 全员名单-基数
    # 读取本地名单
    arraysAll = readSouceGroup()
    # 核心代码：遍历每组对应的查询今日签到的URL
    for group_name, group_url in groups_url.items():
        realUrl = group_url.format(yyyyMMdd)

        # 核心代码：爬虫核心 一切数据的基数
        # 统计组group_name来自网络打卡人员的集合
        # 已签到
        tmpGroup = requestQiandao(realUrl)
        # 统计取这组的人数，目前写死
        tmpAll = getGroupPeopleCount(realUrl, yyyyMMdd)
        print('--------------------------------------------')
        print("网上签到情况={}".format(tmpGroup))
        print('签到情况统计=[{}][实到:{}][应到:{}]'.format(group_name, len(tmpGroup), tmpAll))

        # 写文件用
        fTotal.write("{}：实到{}，应到{}".format(group_name, len(tmpGroup), tmpAll) + os.linesep)
        # 统计用
        group_count[group_name] = len(tmpGroup)

        if len(tmpGroup) != tmpAll:
            print("-->【签到异常】{}应到{}实到{}".format(group_name, len(tmpGroup), tmpAll))
        else:
            group_out_finish.append(group_name)

        # 核心查找没签到的代码，剔除已经签到，剩下就是没有签到，已经签到的
        for i in tmpGroup:
            for j in arraysAll:
                if getLinkSampleStr(i, j) != '':
                    # print('[原始数据={}][实际数据={}]'.format(i, j))
                    arraysAll.remove(j)
                    break

    print('--------------------------------------------')
    # os.linesep代表当前操作系统上的换行符
    fTotal.write('完成打卡的小组:')
    for fg in group_out_finish:
        fTotal.write(fg + "、")
    fTotal.write(os.linesep)
    print("完成打卡的小组：{}".format(group_out_finish))

    print('--------------------------------------------')
    print('-->')
    print("未签到：{}".format(arraysAll))
    print('-->')
    print('--------------------------------------------')
    # 未签到人员名单
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
    sendEmailFile(yyyyMMdd + '打卡', '\n , '.join(arraysAll), fno.name, fWechat.name, fTotal.name)

    print("打开输出目录")
    # os.system("explorer {}".format(yyyyMMdd))

    time.sleep(0.5)

    print("打开生成的没打卡人员名单")
    # os.system("notepad {} ".format(fno.name))

    print("打开生成的微信群发统计消息文件")
    # os.system("notepad {} ".format(fWechat.name))

    print("打开生成的完成小组统计文件")
    # os.system("notepad {} ".format(fTotal.name))

    print("执行结束")
    print("文件保存在根目录")

# 改为自动运行
if __name__ == '__main__':
    # 每天提醒时间
    target = "08:30"
    while True:
        time_now = time.strftime("%H:%M", time.localtime())  # 刷新
        if time_now == target:  # 设置要执行的时间
            # 要执行的代码
            getYi()
            time.sleep(61)  # 停止执行61秒，防止反复运行程序。
        else:
            print('当前时间{},定时任务执行时间{}'.format(time_now, target))
            time.sleep(20)