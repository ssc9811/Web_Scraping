from bs4 import BeautifulSoup
import requests

URL = f"https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}



def search_item(last_page):
    for i in range(1, int(last_page)):
        result = requests.get(f"{URL}&page={i}", headers=headers)
        soup = BeautifulSoup(result.text, "lxml")
        items = soup.find_all("li",{"class":"search-product"})
        for item in items:
            item_name = item.find("div",{"class":"name"}).get_text()
            item_price = item.find("strong",{"class":"price-value"}).get_text()
            item_rating = item.find("em",{"class":"rating"})
            if item_rating:
                item_rating = item_rating.get_text()
            else:
                continue
            item_rating_count = item.find("span",{"class":"rating-total-count"})
            if item_rating_count:
                item_rating_count = item_rating_count.get_text()
                item_rating_count = item_rating_count[1:-1]
            else:
                continue

            if float(item_rating) >= 4.5 and int(item_rating_count) >= 100:
                print(f"상품 이름 : {item_name} 상품 가격 : {item_price} 상품 평점 : {item_rating} ({item_rating_count})")
                print("-"*100)

def last_page():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    page = soup.find("a",{"class":"btn-last disabled"})
    last_page = page.get_text()
    search_item(last_page)

last_page()