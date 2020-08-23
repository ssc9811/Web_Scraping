from bs4 import BeautifulSoup
import requests

URL = f"https://comic.naver.com/webtoon/list.nhn?titleId=736277&weekday=sun"

def rate():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    webtoon = soup.find_all("div",{"class":"rating_type"})
    for webtoons in webtoon:
        rate = webtoons.find("strong").get_text()
        return rate
        
def last_page(max_page):
    for i in range(int(max_page)):
        result = requests.get(f"{URL}&page={i+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        webtoon = soup.find_all("td",{"class":"title"})
        for webtoons in webtoon:
            title = webtoons.get_text(strip=True)
            rink = webtoons.a["href"]
            rinks = f"https://comic.naver.com{rink}"
            print(title, rinks)

def search_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    paginates = soup.find("div",{"class":"paginate"}).find_all("a",{"class":"page"})
    pages = paginates[-1:]
    for page in pages:
        max_page = page.get_text()
    last_page(max_page)
    
search_page()