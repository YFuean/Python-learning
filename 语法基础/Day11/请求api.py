'''
requests请求api，用字典和列表保存为json
'''
import json
import requests

resp = requests.get(
    'http://api.tianapi.com/txapi/ncovabroad/index?key=bc90444f3f244b0eb39cd743f62d7c02')
newslist = json.loads(resp.text)['newslist']
result = []
data = './res/data.json'
for news in newslist:
    temp_dict = {}
    temp_dict['continents'] = news['continents']
    temp_dict['province_name'] = news['provinceName']
    temp_dict['cured_count'] = news['curedCount']
    temp_dict['dead_count'] = news['deadCount']
    result.append(temp_dict)
with open(data, 'w') as f:
    json.dump(result, f)
