import csv
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

    # 사이트 열기 : 아이폰 13 검색 결과
    browser.get(
        "https://search.shopping.naver.com/search/all?query=%EC%95%84%EC%9D%B4%ED%8F%B0%2013&frm=NVSHATC&prevQuery=%EC%95%84%EC%9D%B4%ED%8F%B013")

    while True:
        # 스크롤 내리기
        before_h = browser.execute_script("return window.scrollY")

        browser.find_element(by=By.CSS_SELECTOR, value="body").send_keys(Keys.END)
        time.sleep(1)

        after_h = browser.execute_script("return window.scrollY")

        if before_h == after_h:
            break

    # csv 파일
    with open("data.csv", "w", encoding="UTF-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # 데이터 가져오기
        items = browser.find_elements(by=By.CSS_SELECTOR, value=".basicList_item__2XT81")
        for item in items:
            name = item.find_element(by=By.CSS_SELECTOR, value=".basicList_link__1MaTN").text
            try:
                price = item.find_element(by=By.CSS_SELECTOR, value=".price_num__2WUXn").text
            except:
                price = "판매중단"
            link = item.find_element(by=By.CSS_SELECTOR, value=".basicList_link__1MaTN").get_attribute("href")

            csv_writer.writerow([name, price, link])
