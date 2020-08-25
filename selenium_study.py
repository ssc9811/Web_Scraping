from selenium import webdriver

# 크롬을 통한 selenium 사용
browser = webdriver.Chrome()

# 전체 화면
browser.maximize_window() 

# 사이트 이동
browser.get("http://naver.com")

# send_keys() : 입력
browser.find_element_by_id("query").send_keys("realy")

# click() : 클릭
browser.find_element_by_id("search_btn").click()

#elements = find_all , xpath도 받아올수 있음.
browser.find_elements_by_xpath

# html 정보 출력
print(browser.page_source)

# 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit() # 전체 브라우저 종료



