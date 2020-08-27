import requests
from bs4 import BeautifulSoup

def creat_soup(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "lxml")
    return soup

def google_new():
    URL = "https://news.google.com/topstories?hl=ko&gl=KR&ceid=KR:ko"
    soup = creat_soup(URL)
    news = soup.find_all("h3",{"class":"ipQwMb"})
    for i ,new in enumerate(news):
        title = new.get_text()
        rink = new.a["href"]
        print(f"----------{i+1}번째 기사----------")
        print(f"{title}")
        print(f"https://news.google.com{rink}")