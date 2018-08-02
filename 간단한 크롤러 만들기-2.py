import requests as rq
from bs4 import BeautifulSoup as B

base_url='https://pjt3591oo.github.io/'
page_path='/page%d'
page=2

res=rq.get(base_url)
soup=B(res.content, 'lxml')

posts=soup.select('body main.page-content div.wrapper div.home div.p')

for post in posts:
    title=post.find('h3').text.strip()
    descript=post.find('h4').text.strip()
    author=post.find('span').text.strip()
    print(title, descript, author +"\n")
    
while True:
    sub_path=page_path%(page)
    page+=1
    res=rq.get(base_url + sub_path)

    if(res.status_code !=200):
        break

    soup=B(res.content, 'lxml')
    
    posts=soup.select('body main.page-content div.wrapper div.home div.p')

    for post in posts:
        title=post.find('h3').text.strip()
        descript=post.find('h4').text.strip()
        author=post.find('span').text.strip()
        print(title, descript, author +"\n")
        

    
        
