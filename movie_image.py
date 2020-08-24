import requests
from bs4 import BeautifulSoup

URL = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}

result = requests.get(URL, headers=headers)
soup = BeautifulSoup(result.text, "lxml")
images = soup.find_all("img",{"class":"thumb_img"})

for idx, image in enumerate(images): #enumerate 배열에서 값과 idx값을 같이 나오게함
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https:" + image_url

    print(image_url)
    image_res = requests.get(image_url)

    with open(f"movie{idx+1}.jpg", "wb") as f:
        # f.write(image_res.content)
        print(image_res.content)

    if idx >= 4:
        break