'''
爬取实验楼所有课程信息
xpath和tree结合获取节点信息
关键词统计数据，比如java,c课程的数量
'''
import requests
from lxml import html


def crawl():
    course_list = []
    for num in range(1, 26):
        url = 'https://www.shiyanlou.com/courses/?page='+str(num)
        content = requests.get(url)
        tree = html.fromstring(content.text)
        course_names = tree.xpath('//h6[@class="course-name"]/text()')
        course_descriptions = tree.xpath(
            '//div[@class="course-description"]/text()')
        course_covers = tree.xpath('//img[@class="cover-image"]/@src')
        for index in (0, len(course_names)-1):
            temp_dict = {}
            temp_dict['name'] = course_names[index].strip()
            temp_dict['description'] = course_descriptions[index].strip()
            temp_dict['cover'] = course_covers[index]
            course_list.append(temp_dict)
    return course_list


if __name__ == '__main__':
    list = crawl()
    print(len(list))
