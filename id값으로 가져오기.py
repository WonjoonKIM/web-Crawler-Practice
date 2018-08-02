from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
        <body> <p>test1</p> <p id='d'>test2</p> <p>test3</p>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.find_all(id='d'))
