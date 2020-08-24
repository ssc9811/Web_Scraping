import csv
import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

filename = "시가 총액.csv"
f = open(filename , "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") #변환
#['N', '종목명', '현재가', '전일비', '등락률', '액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE']
writer.writerow(title)

def list(last_page):
    for i in range (0 , int(last_page)):
        result = requests.get(f"{URL}&page={i+1}", headers=headers)
        soup = BeautifulSoup(result.text, "lxml")
        rows = soup.find("table",{"class":"type_2"}).find("tbody").find_all("tr")
        for row in rows:
            colums = row.find_all("td")
            if len(colums) <= 1:
                continue
            data = [colum.get_text().strip() for colum in colums] #find_all 값을 get_text로 가져오기 위해선 for문 사용해야함.
            data = data[:-1]
            writer.writerow(data)
        

def last_page():
    result = requests.get(URL, headers=headers)
    soup = BeautifulSoup(result.text, "lxml")
    page = soup.find("td",{"class":"pgRR"}).find("a")["href"]
    last_page = page[-2:]
    list(last_page)

last_page()
