from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body> <p>test1</p> <p class='d'>test2</p> <p class='c'>test3</p>
        <a>wonjoon</a> <b>KIM</b>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.find_all('p', text='test1'))
print(soup.find_all('p', text='t'))
