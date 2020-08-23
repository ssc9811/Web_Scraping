# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
# result = requests.get(URL, headers=headers)  -- 웹 서버에 내가 기계가 아니라고 알려주는 표현(?)

# from bs4 import BeautifulSoup
# import requests

# URL = f"https://comic.naver.com/webtoon/list.nhn?titleId=736277&weekday=sun"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

# result = requests.get(f"{URL}&page={1}", headers=headers)
# soup = BeautifulSoup(result.text, "lxml")
# table = soup.find_all("tr")
# for tables in table:
#     print(tables)

for i in range(1, 15):
    print(i)