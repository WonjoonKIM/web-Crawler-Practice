from bs4 import BeautifulSoup as B
from bs4 import NavigableString as N, Tag as T

html="""<html><head><title>test site</title></head>
        <body> <p>test1</p> <p>test2</p> <p>test3</p>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.find_all('title'))
print(soup.find_all('p'))
    

