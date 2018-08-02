from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
      <body><p><span>test1</span><span>test2</span></p>
      </body></html>"""

soup=B(html,'lxml')

tag_span=soup.span
tag_title=soup.title

span_parent=tag_span.parent
title_parent=tag_title.parent

print('태그')
print(tag_span)
print(tag_title)

print('span 부모태그')
for parent in span_parent:
    print(parent)
print('title 부모태그')
for parent in title_parent:
    print(parent)
