from selenium import webdriver

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

