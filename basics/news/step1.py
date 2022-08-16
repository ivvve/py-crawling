import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90"
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(markup=html, features="html.parser")
    news_titles = soup.select(".news_tit")
    for news_title in news_titles:
        link = news_title.attrs["href"]  # a tag의 href 속성을 가져온다
        print(f"Text: {news_title.text}, Link: {link}")
