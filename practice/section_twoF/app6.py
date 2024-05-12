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

time.sleep(2) #창이 다 뜰때가지 기다려야됨

element = driver.find_element(By.CSS_SELECTOR,'._ab37') # 요소 찾기는 이렇게 아이디는 #

print(element.text)