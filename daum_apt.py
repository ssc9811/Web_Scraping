import requests
from bs4 import BeautifulSoup

URL = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

result = requests.get(URL, headers=headers)
soup = BeautifulSoup(result.text, "lxml")
tables = soup.body.find("tbody").find_all("tr")

for index, table in enumerate(tables):
    column = table.find_all("td")
    print(column)
    print(f"======={index}=======")
    print(f"거래 : {column[0].get_text()}")
    print(f"면적 : {column[1].get_text()}(공급/전용)")
    print(f"가격 : {column[2].get_text()}(만원)")
    print(f"동 : {column[3].get_text()}")
    print(f"층 : {column[4].get_text()}")