from selenium import webdriver

url="https://www.daum.net/"

driver=webdriver.Chrome('chromedriver')
driver.get(url)

selected_tags_a=driver.find_elements_by_css_selector('a')

for i in selected_tags_a:
    print(i.text, i.tag_name)
    i.click()


#메인 페이지에서 돔을 가져오고 다른 페이지로 넘어가면 메인페이지에서
#가져온 도에 접근할 수 없어서 에러가 나고
#click을 페이지 이동하는 용도로 사용하면 안된다.
