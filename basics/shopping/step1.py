import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

if __name__ == '__main__':
    # 브라우저 생성
    browser = webdriver.Chrome("/Users/son/Downloads/chromedriver")

    # 사이트 열기
    browser.get("https://naver.com")
    browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지 기다려준다

    # 클릭
    browser.find_element(by=By.CSS_SELECTOR, value="a.nav.shop").click()
    time.sleep(1)

    # 검색
    search_input = browser.find_element(by=By.CSS_SELECTOR, value="input._searchInput_search_input_QXUFf")
    search_input.click()
    search_input.send_keys("아이폰 13")
    search_input.send_keys(Keys.ENTER)
