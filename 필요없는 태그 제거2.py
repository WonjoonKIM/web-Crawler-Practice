from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body>
        <p id='i' class='a'>test1</p> <p class='d'>test2</p> <p class='c'>test3</p>
        <a>WonJoon</a><b>KIM</b>
        </body></html>"""

soup=B(html, 'lxml')

for tag in soup.select('p'):
    print(tag.extract())

#for tag in soup.find_all(['p'], 'a']):
#   print(tag.extract())   p부터 a까지 제거함  

print('제거 완료')
print(soup)
