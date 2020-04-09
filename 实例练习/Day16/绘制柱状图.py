'''
pyecharts绘制柱状图
'''

from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType
# 内置主题类型 pyecharts.globals.ThemeType
# 有LIGHT DARK WHITE CHALK ESSOS INFOGRAPHIC等

# 第一幅图，数据固定
bar = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(['服饰', '箱包', '鞋帽', '电子', '数码', '户外'])
    .add_yaxis('京东', [5, 23, 32, 12, 54, 90])
    .add_yaxis('天猫', [15, 6, 32, 74, 54, 90])
    .set_global_opts(title_opts=opts.TitleOpts(title='电商销售对比'))
)
bar.render(path='./res/电商销售对比.html')

# 第二幅图，数据分离
items = ['Java', 'C', 'Python', 'C++', 'JavaScript', 'C#', 'PHP', 'SQL']
data_list1 = [188, 166, 110, 108, 90, 80, 55, 45]
data_list2 = [190, 160, 140, 100, 80, 70, 50, 40]
bar1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.CHALK))
    .add_xaxis(items)
    .add_yaxis('2020年', data_list1)
    .add_yaxis('2019年', data_list2)
    .set_global_opts(title_opts=opts.TitleOpts(title='编程语言排行', subtitle='2019-2020'))
)
bar1.render(path='./res/编程语言排行.html')
