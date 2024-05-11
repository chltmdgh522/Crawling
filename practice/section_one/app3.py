import requests
from bs4 import BeautifulSoup


def crawling(num):
    data = requests.get(
        f'https://s.search.naver.com/p/review/47/search.naver?ssc=tab.blog.all&api_type=4&query=%EC%82%AC%EA%B3%BC&start={num}&nx_search_query=&nx_and_query=&nx_sub_query=&ac=1&aq=0&spq=0&sm=tab_jum&nso=&prank=61&ngn_country=KR&lgl_rcode=11237101&fgn_region=&fgn_city=&lgl_lat=37.494216&lgl_long=126.720071&enlu_query=IggCAGmCULhPAAAAuGDqbIuW1YP0vEg6kPSZvKThDfucDIms%2FudRHfdG8G6lrY51DY46PeYIbwkbS8xiudItAzyH7S8Eg51IkSBppni9mX5I8W2GLmLj6MQogxQ%3D&abt=')
    soup = BeautifulSoup(data.text.replace('\\', ''), 'html.parser')  # 문자형태로 해야지 replace 할 수 있음
    text = soup.select('a.title_link')[0]['href'] # 제목이면 그냥 .text
    return text

f=open('b.txt','w')
for i in range(10):
    s = crawling(i)
    f.write(s)
    f.write("\n")


