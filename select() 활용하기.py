from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body>
        <p id='i' class='a'>test1</p> <p class='d'>test2</p> <p class='c'>test3</p>
        <a>WonJoon</a><b>KIM</b>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.select('p'))     #모든 p요소 찾기
print(soup.select('p.d'))   #클래스가 d인 모든 요소 찾기
print(soup.select('#i'))    #id가 i인 모든 요소
print(soup.select('p#i'))   #태그가 p이고 아이디가 i인 모든 요소를 찾아준다.
