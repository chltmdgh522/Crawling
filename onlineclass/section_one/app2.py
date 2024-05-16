import requests
import urllib.request
from bs4 import BeautifulSoup
import os



def crawling(blank):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={blank}') #변수는 f랑 {} 이거 필수
    soup = BeautifulSoup(data.content, 'html.parser')
    text = soup.find_all('strong', id="_nowVal")[0].text
    tah__text = soup.find_all('span', class_="tah")[0].text

    return text


crawling('005930')

f=open('a.txt' ,'w')

list = ['005930', '066575', '005380', '035720', '034220', '003490']

for i in list:
    s = crawling(i)
    f.write(s)
    f.write("\n")

# data = requests.get('https://finance.naver.com/item/sise.nhn?code=066575')
#
# soup = BeautifulSoup(data.content, 'html.parser')
# print(soup.find_all('strong', id="_nowVal")[0].text)
#
# print(soup.find_all('span', class_="tah")[0].text)
