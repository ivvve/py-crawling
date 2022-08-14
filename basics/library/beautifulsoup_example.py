import requests
from bs4 import BeautifulSoup

response = requests.get("https://naver.com")
html = response.text

soup = BeautifulSoup(markup=html, features="html.parser")
home_btn = soup.select_one("#NM_set_home_btn")
print(home_btn.text)
