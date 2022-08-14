import requests

response = requests.get("https://naver.com")
html = response.text
print(html)
