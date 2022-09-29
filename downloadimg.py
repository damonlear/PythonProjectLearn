import requests
import os
import logging


def download(imp, index) :

     os.makedirs('./file', exist_ok=True)
     headers={
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
     }
     #发送get请求图片url
     r=requests.get(imp.format(index),headers=headers)
     # wb 以二进制打开文件并写入，文件名不存在会创建
     with open("./file/{}.jpg".format(index),'wb') as f:
          f.write(r.content) #写入二进制内容

     logging.error(imp.format(index))


if __name__ == '__main__':

     log = logging.getLogger()
     log.setLevel("ERROR")

     logging.error("请输入要批量下载的文件路径，并用{}号作为占位符，替换页码")
     imp = input()

     logging.error("请输入要批量下载的数量，默认从0开始")
     index = input()

     for i in range(int(index)):
          download(imp, i)
