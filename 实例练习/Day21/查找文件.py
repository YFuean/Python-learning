"""
查找当前目录所有文件
"""
import os
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 内置主题类型 pyecharts.globals.ThemeType
# 有LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC等

text = 0
json = 0
html = 0
csv = 0
jpg = 0


def get_all(cwd):
    result = []
    # 遍历当前目录，获得文件列表，
    get_dir = os.listdir(cwd)
    # print(get_dir)
    for i in get_dir:
        # 把第一步获取的文件加入路径
        # pritn(i)
        sub_dir = os.path.join(cwd, i)
        # print(sub_dir)
        # 如果当前文件仍然是文件类, 递归调用
        if os.path.isdir(sub_dir):
            get_all(sub_dir)
        else:
            # 如果当前路径不是文件类,则把文件名放入列表
            file_name = os.path.basename(sub_dir)

            if file_name.split(".")[-1] == "text":
                global text
                text += 1
            elif file_name.split(".")[-1] == "json":
                global json
                json += 1
            elif file_name.split(".")[-1] == "html":
                global html
                html += 1
            elif file_name.split(".")[-1] == "jpg":
                global jpg
                jpg += 1
            elif file_name.split(".")[-1] == "csv":
                global csv
                csv += 1
            result.append(file_name)
    return result


def drawPie(text, json, csv, jpg, html):
    x_data = ['text', 'json', 'csv', 'jpg', 'html']
    y_data = [text, json, csv, jpg, html]

    pie = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.INFOGRAPHIC))
        .add(
            series_name="文件类型",
            data_pair=[list(z) for z in zip(x_data, y_data)]
        )
        .set_global_opts(title_opts=opts.TitleOpts(title='文件类型饼图'))
    )
    pie.render("./res/文件类型饼图.html")


if __name__ == "__main__":
    # 取得当前目录：home\yfuean\python-learning,拼上子目录
    cur_path = os.getcwd() + '/res'
    # print(cur_path)
    # 调用函数，统计res目录下文件
    print('当前目录的所有文件', get_all(cur_path))
    drawPie(text, json, csv, jpg, html)
