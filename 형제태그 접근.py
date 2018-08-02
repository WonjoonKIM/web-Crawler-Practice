from bs4 import BeautifulSoup as B

html="""<html><head><title>test site</title></head>
      <body><p><span>test1</span><span>test2</span></p>
      </body></html>"""

soup=B(html,'lxml')

tag_span=soup.span

a=tag_span.next_sibling
b=a.previous_sibling

print(a)
print(b)
