import requests as rq
from bs4 import BeautifulSoup as B

base_url='https://mail.naver.com/?n=1526972247690&v=f'
page_path='/page%d'
page=2

res=rq.get(base_url)
soup=B(res.content, 'lxml')

posts=soup.select('body div.wrap div#container div#section_cen div#section_cen_fix div#content div#cont_flex_area div.divList unselectable div.list_for_view ol.mailList preview_none sender_context li div.mTitle')
for post in posts:
    author=post.find('span').text.strip()
    print(author +"\n")
    
while True:
    sub_path=page_path%(page)
    page+=1
    res=rq.get(base_url + sub_path)

    if(res.status_code !=200):
        break

    soup=B(res.content, 'lxml')
    
    posts=soup.select('body div.wrap div#container div#section_cen div#section_cen_fix div#content div#cont_flex_area div.divList unselectable div.list_for_view ol.mailList preview_none sender_context li div.mTitle')
                      
    for post in posts:
        author=post.find('span').text.strip()
        print(author +"\n")
        
