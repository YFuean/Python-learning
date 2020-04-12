"""
继承Thread类创建自定义的线程类
"""
from time import time
from threading import Thread
import requests

# 继承Thread类创建自定义的线程类


class DownloadHandle(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open('./res/img/' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 使用了知乎数据接口

    resp = requests.get(
        'https://www.zhihu.com/api/v4/roundtables?limit=10&offset=10')
    # 将服务器返回的JSON格式的数据解析为字典
    data_model = resp.json()
    for mm_dict in data_model['data']:
        url = mm_dict['logo']
        # 通过多线程的方式实现图片下载
        DownloadHandle(url).start()


if __name__ == '__main__':
    main()
