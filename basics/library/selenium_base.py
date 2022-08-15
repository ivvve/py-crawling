from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
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
