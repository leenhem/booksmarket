# _*_ coding:UTF-8 _*_
# from urllib import request
import requests
import random
from bs4 import BeautifulSoup

def get_content(url,data=None):
    header={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.235'
    }
    # timeout = random.choice(range(80, 180))
    timeout = random.choice(range(8000, 18000))
    req=requests.get(url,headers=header,timeout=timeout)
    req.encoding='utf-8'
    return req.text
def get_data(html_text):
    final=[]
    bs=BeautifulSoup(html_text,"html.parser")
    body=bs.body
    data=body.find('div',{'class':'in_box'})
    for item in data:
        i=item.find('h2')
        if i is None:
            i=item.find('h3')
        if type(i) != type(1):
            link,name=i.find('a')['href'],i.find('a')['title']
            final.append([link,name])
    return final
def get_video(url):
    html_text=get_content(url)
    bs=BeautifulSoup(html_text,"html.parser")
    for i in bs.find_all('a'):
        href=i.get('href')
        if '.mp4' in href and href != '':
            break
    return href
# if __name__ == '__main__':
#     url="http://www.9558.tv"
#     html_text=get_content(url=url)
#     url_list=get_data(html_text)
#     for item in range(0,len(url_list)):
#         print(url_list[item])
#         url_list[item].append(get_video(url_list[item][0]))
