import time

import pyperclip
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

    # 로그인
    browser.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")

    id_input = browser.find_element(by=By.ID, value="id")
    pyperclip.copy("id")  # id 입력
    id_input.send_keys(Keys.COMMAND, "v")
    time.sleep(2)

    password_input = browser.find_element(by=By.ID, value="pw")
    pyperclip.copy("password")  # password 입력
    password_input.send_keys(Keys.COMMAND, "v")
    time.sleep(2)

    browser.find_element(by=By.ID, value="log.login").click()
