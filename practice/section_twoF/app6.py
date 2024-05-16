import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.instagram.com/')

time.sleep(2)  # 창이 다 뜰때가지 기다려야됨
#
# element = driver.find_element(By.CSS_SELECTOR,'input[name="username"]') # 요소 찾기는 이렇게 아이디는 # 클래스는. name은 바로 앞에
# print(element.text)

e = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
e.send_keys('csh_crawling_test')
e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
e.send_keys("qkek@@0312")
e.send_keys(Keys.ENTER)  # 로그인

time.sleep(4)
# 페이지 이동
driver.get("https://www.instagram.com/explore/tags/%EC%BD%94%EB%82%9C/")
driver.implicitly_wait(10)  # 아래 요소가 없으면 10초간 기다리자
driver.find_element(By.CSS_SELECTOR, '._aagw').click()  # 이 클래스가 많음 근데 element 쓰면 맨 위에꺼 하나만 찾아주고 elements면 전부 찾아서 리스트에 담아줌

time.sleep(10)
# 사진 저장
img_url = driver.find_element(By.CSS_SELECTOR, '.x5yr21d.xu96u03.x10l6tqk.x13vifvy.x87ps6o.xh8yej3').get_attribute('src')
if img_url:
    print("이미지 URL:", img_url)
    urllib.request.urlretrieve(img_url, '1.jpg')
    print("이미지 다운로드 완료")
else:
    print("이미지 URL이 없습니다.")
