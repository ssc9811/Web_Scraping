from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()

URL = "https://flight.naver.com/flights/"
browser.get(URL)

browser.find_elements_by_class_name("tit_airport")[1].click()
browser.find_element_by_link_text("제주").click()

browser.find_element_by_class_name("txt_trip").click()
browser.find_elements_by_link_text("29")[0].click()
browser.find_elements_by_link_text("12")[1].click()
browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]")))
    # 성공했을 때 동작 수행    
    print(elem.text) # 첫번째 결과 출력
finally:
    browser.quit()
