import requests
from bs4 import BeautifulSoup

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
# print(data.content) # 사이트 내용 근데 깨져서 bs4에 넣어야됨
# print(data.status_code) # 사이트 상태

soup = BeautifulSoup(data.content, 'html.parser') #이렇게 하면 이쁘게 나옴
print(soup.find_all('strong', id="_nowVal")[0].text) #리스트로 나옴 text라고 쓰면 태그들 싹다 지우고 data만 나옴

print(soup.find_all('span', class_="tah")[25].text)  #class는 예약어라서 _이거 붙여주기,  또한 class 명이 2개이상이면 하나만쓰기