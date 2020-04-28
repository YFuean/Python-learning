"""
中文文本情感分析
"""
from snownlp import SnowNLP

text = '噫吁嚱，危乎高哉！蜀道之难，难于上青天！蚕丛及鱼凫，开国何茫然！'
s = SnowNLP(text)
# 分词
print(s.words)
# 词性标注
tags = [x for x in s.tags]
print(tags)
# 断句
print(s.sentences)
# 拼音
print(s.pinyin)

# 情绪判断，返回值为正面情绪的概率，越接近1表实正面情绪。越接近0表示负面情绪
# text1 = '春风得意马蹄疾，一日看尽长安花'
text2 = '万里悲秋常作客，百年多病独登台'
text1 = '春风得意马蹄疾，一日看尽长安花'
text3 = '里约热内卢的奶牛拿榴莲牛奶'
s1 = SnowNLP(text1)
s2 = SnowNLP(text2)
s3 = SnowNLP(text3)
print(text1, s1.sentiments)
print(text2, s2.sentiments)
print(text3, s3.sentiments)

# 关键字抽取
text3 = '里约热内卢的奶牛拿榴莲牛奶以折足之姿跑到委内瑞拉拿了蜂花护发素送给红鲤鱼与绿鲤鱼与驴'
s3 = SnowNLP(text3)
print(s3.keywords(limit=5))
print(s3.summary(limit=4))
