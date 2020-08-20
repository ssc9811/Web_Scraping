from bs4 import BeautifulSoup
import requests

URL = "https://comic.naver.com/index.nhn"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "html.parser")
box_rank = soup.find("ol",{"class":"asideBoxRank"})
titles = box_rank.find_all("a")
for title in titles:
    lank = title.get_text()
    print(lank)