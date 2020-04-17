"""
导入词云制作库wordcloud和中文分词jieba
"""
import jieba
import wordcloud
w = wordcloud.WordCloud(
    width=1000,
    height=700,
    background_color='#70d0b2',
    colormap='PuBu',
    font_path='./res/fonts/SimHei.ttf')


# 调用jieba的cut()方法对原始文本进行中文分词，得到string
txt = '说个数据吧，某猎头的根据简历投递情况进行的统计整个开发行业程序猿大约50万人，真正做敲代码工作的大约是30万人，\
你问我其他20万是干嘛emmm我也不太清楚，可能是管理，架构…其中大约25万都是基层码农，培训学校输出相当大的一部分人。 \
具有比较全面计算机从业能力的不到10万人。这些人大多也是做上层应用，中国有能力从事底层开发的人就更少了， \
国内某个大厂整个公司有能力从事编译器开发的人不到10人，这些人还是通过公司这几年专项招聘进来，公司是非常希望拥有这样的人才 \
今年的数据不太了解，毕竟收购了个做这方面的公司，可能有些许增加。底层开发人员少，是公司CTO都非常头疼的问题。\
中国软硬件如果想有进步，仍然是需要非常大量的人才。整个中国开发行业是处于围城的状态，外边的人抱怨找不到工作，\
里边的人抱怨招不到人。所以中国软硬件现阶段是机会不缺，人也不缺，但是缺人才。'
txtlist = jieba.lcut(txt)
string = "".join(txtlist)
# 将string变量传入w的generate()方法，给词云输入文字
w.generate(string)
# 将词云图片导出到当前文件夹
w.to_file('./res/img/output3.png')
