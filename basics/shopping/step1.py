import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == '__main__':
    # Web Driver
    service = Service(executable_path=ChromeDriverManager().install())

    # Driver Options
    driver_options = Options()
    driver_options.add_experimental_option("detach", True)  # 프로세스 종료 후 브라우저 꺼짐 방지
    driver_options.add_experimental_option("excludeSwitches", ["enable-logging"])  # 불필요한 에러 메세지 없애기

    browser = webdriver.Chrome(service=service, options=driver_options)

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
