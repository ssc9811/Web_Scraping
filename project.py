import requests
from bs4 import BeautifulSoup

# 구글 헤드라인 기사
URL = "https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko"

result = requests.get(URL)
soup = BeautifulSoup(result.text, "lxml")
news = soup.find_all("h3",{"class":"ipQwMb"})
for new in news:
    title = new.get_text()
    rink = new.a["href"]
    print("-"*100)
    print(f"{title}")
    print(f"https://news.google.com{rink}")