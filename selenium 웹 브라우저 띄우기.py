from selenium import webdriver

url="https://www.naver.com"

driver=webdriver.Chrome('chromedriver')
driver.get(url)

selected_id=driver.find_element_by_id("PM_ID_ct")

print(selected_id)
print('다음``')
print(selected_id.tag_name)
print('다음~~')
print(selected_id.text)
