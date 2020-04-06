'''
爬取知乎一个专栏的所有粉丝数据并存入数据库
'''
import requests
import json
import pymysql
import time


def crawl():
    followers_data = []
    for offset in range(2500, 3000, 20):
        time.sleep(1)
        url = "https://www.zhihu.com/api/v4/columns/zuimei/followers?include=data%5B*%5D.follower_count%2Cgender%2Cis_followed%2Cis_following&limit=20&offset=" + \
            str(offset)
        print(url)
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        followers_data += response.json().get("data")
    return followers_data


def data_inster(followers_data):
    db = pymysql.connect("localhost", "root", "", "db_python")
    cursor = db.cursor()
    val = []
    for dic in followers_data:
        item = (dic['id'], dic['name'], dic['url'], dic['gender'],
                dic['avatar_url'], dic['follower_count'])
        val.append(item)
    sql = "INSERT INTO t_follower (id,name,url,gender,avatar_url,follower_count) VALUES (%s,%s,%s,%s,%s,%s)"
    try:
        cursor.executemany(sql, val)
        db.commit()
    except:
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    list = crawl()
    print(list)
    data_inster(list)
