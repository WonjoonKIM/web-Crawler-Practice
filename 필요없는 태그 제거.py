from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body>
        <p id='i' class='a'>test1</p> <p class='d'>test2</p> <p class='c'>test3</p>
        <a>WonJoon</a><b>KIM</b>
        </body></html>"""

soup=B(html, 'lxml')

a=soup.body.extract()

print('제거항목')
print(a)
print('제거완료')
print(soup)
