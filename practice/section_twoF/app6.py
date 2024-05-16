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
e.send_keys(Keys.ENTER) #로그인