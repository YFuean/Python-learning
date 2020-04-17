"""
基础词云
"""
import wordcloud
import random
# 创建词韵
w = wordcloud.WordCloud()
# 生成字符串生成词云
w.generate(' From tomorrow on, I will be a happy man. Grooming, chopping, and traveling all over the world')
# 生成本地图片
w.to_file('./res/img/output1.png')


# 创建词云对象，设置次云照片宽、高、字体、背景颜色等参数
# 中文字体需要提前下载中文字体文件
w = wordcloud.WordCloud(width=1000, height=700,
                        background_color='#eeeeee', font_path='./res/fonts/SimHei.ttf')
w.generate('从明天起，做一个幸福的人，喂马，劈柴，周游世界.从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')
w.to_file('./res/img/output2.png')
