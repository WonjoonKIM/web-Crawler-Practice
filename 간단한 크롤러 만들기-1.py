import requests as rq
from bs4 import BeautifulSoup as B

base_url='https://edward.kmu.ac.kr/nx/'
res=rq.get(base_url)
soup=B(res.content, 'lxml')

posts=soup.select('body main.page-content div.wrapper div.home div.p')

for post in posts:
    title=post.find('h3').text.strip()
    descript=post.find('h4').text.strip()
    author=post.find('span').text.strip()
    print(title, descript, author +"\n")
    



