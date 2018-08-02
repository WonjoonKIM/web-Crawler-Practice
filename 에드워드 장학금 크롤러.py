import requests as rq
from bs4 import BeautifulSoup as B

base_url='https://edward.kmu.ac.kr/nx/'
#page_path='/page%d'
#page=2

res=rq.get(base_url)
soup=B(res.content, 'lxml')

posts=soup.select('body div.mainframe_VFrameSet_HFrameSet_VFrameSet1_WorkFrame_Child_M503056_form_div_Work_Tab01_tabpage9_grd_scho101_body_gridrow_7_cell_7_4GridCellTextContainerElement')
                            mainframe_VFrameSet_HFrameSet_VFrameSet1_WorkFrame_Child_M503056_form_div_Work_Tab01_tabpage9_grd_scho101_body_gridrow_4_cell_4_4GridCellTextContainerElement
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
        

    
        
