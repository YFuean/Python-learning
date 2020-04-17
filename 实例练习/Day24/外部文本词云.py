"""
外部文本词云
"""
import wordcloud
import random

f = open('./res/txt/计算机应届生月薪大多是多少.txt', encoding='utf-8')
txt = f.read()

# 更换背景颜色和整体风格
w = wordcloud.WordCloud(
    width=1000,
    height=800,
    scale=2,
    max_font_size=80,
    background_color='#e5f2ff',
    colormap='PuRd',
    font_path='./res/fonts/SimHei.ttf')

# 将txt变量传入

w.generate(txt)
w.to_file('./res/img/output4.png')
