from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body> <p>test1</p> <p class='d'>test2</p> <p class='c'>test3</p>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.find_all('p', class_='d'))
print(soup.find_all('p', 'c'))
#클래스는 굳이 class_키워드를 붙이지 않고 비워도 됩니다.
