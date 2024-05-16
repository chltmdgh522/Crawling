import requests
import urllib.request
from bs4 import BeautifulSoup
import os

data = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')
# print(data.content) # 사이트 내용 근데 깨져서 bs4에 넣어야됨
# print(data.status_code) # 사이트 상태

soup = BeautifulSoup(data.content, 'html.parser')  # 이렇게 하면 이쁘게 나옴
print(soup.find_all('strong', id="_nowVal")[0].text)  # 리스트로 나옴 text라고 쓰면 태그들 싹다 지우고 data만 나옴

print(soup.find_all('span', class_="tah")[25].text)  # class는 예약어라서 _이거 붙여주기,  또한 class 명이 2개이상이면 하나만쓰기

print(soup.find_all('em', class_="no_down")[1].text)  # 이거는 해체되어있는 각요소들은 부모로 불러오기

print(soup.select('.gray .f_down em')[0].text) # 클래스명은 . 붙이기 즉 #은 id  그리고 띄어쓰기 내부 요소 즉 em이  클래스 나 아이디 이름 없을 때 유리

image = soup.select('#img_chart_area')[0] #이미지   근데 이미지 다운 받고 싶으면 src로 ㄱㄱ
print(image['src']) # 이미지 경로

# 이미지를 저장할 디렉토리 경로
save_dir = '/onlineclass/img'

# 디렉토리가 존재하지 않으면 생성
os.makedirs(save_dir, exist_ok=True)

# 이미지 저장
urllib.request.urlretrieve(image['src'], os.path.join(save_dir, 'tmdgh.jpg'))