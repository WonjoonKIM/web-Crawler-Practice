from bs4 import BeautifulSoup as B
import re #정규식을 사용하기 위해 re라는 모듈을 이

html="""<html><head><title>test site</title></head><body>
        <div><p id='i' class='a'>test1</p> <p class='d'>test2</p></div>
        <p class='d'>test3</p> <a href="https://www.naver.com">a tag</a>
        <b>b tag</b>
        </body></html>"""

soup=B(html, 'lxml')

print(soup.find_all(class_=re.compile('d')))    #클래스 값에 d가 포함된 요소
print(soup.find_all(id=re.compile('i')))        #아이디값에 i가 포함
print(soup.find_all(re.compile('t')))           #태그에 t가 포함된 요소
print(soup.find_all(re.compile('^t')))          #태그 이름이 t로 시작하는 요소
print(soup.find_all(href=re.compile('/')))      #href에 /가 포함된 요소
