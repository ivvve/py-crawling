import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    query = input("검색어: ")
    last_page = int(input("마지막 페이지 번호: "))
    current_page = 1

    for i in range(1, last_page * 10, 10):
        print(f"Page: {current_page}, start: {i}")
        current_page += 1

        url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}&start={i}"
        response = requests.get(url)
        html = response.text

        soup = BeautifulSoup(markup=html, features="html.parser")
        news_titles = soup.select(".news_tit")
        for news_title in news_titles:
            link = news_title.attrs["href"]  # a tag의 href 속성을 가져온다
            print(f"Text: {news_title.text}, Link: {link}")
