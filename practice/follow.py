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

e = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
e.send_keys('')
e = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
e.send_keys("")
e.send_keys(Keys.ENTER)  # 로그인

time.sleep(4)
# 페이지 이동
driver.get("https://www.instagram.com/skuukzky/followers/")
driver.implicitly_wait(10)  # 아래 요소가 없으면 10초간 기다리자


for i in range(0, 200):
    # 팔로우 버튼 클릭
    driver.find_elements(By.CSS_SELECTOR, '._acan._acap._acas._aj1-._ap30')[i].click()
    print(str(i)+"번쨰")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(1)



