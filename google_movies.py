from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

URL = "https://play.google.com/store/movies/top"
browser.get(URL)

import time
interval = 2 # 2초에 한번씩 스크롤 내림

# 현재 문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

# 반복 수행
while True:
    # 스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # 페이지 로딩 대기
    time.sleep(interval)

    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break

    prev_height = curr_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
# movie = soup.find_all("div",{"class":["ImZGtf mpg5gc","Vpfmgd"]}) # 여러개 가져오는 방법
movie = soup.find_all("div",{"class":"Vpfmgd"})
print(len(movie))

for movies in movie:
    title = movies.find("div",{"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

browser.quit()