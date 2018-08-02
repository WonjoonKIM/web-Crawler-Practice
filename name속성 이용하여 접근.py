from selenium import webdriver

url="https://www.naver.com"

driver=webdriver.Chrome('chromedriver')
driver.get(url)

selected_name=driver.find_element_by_name("query")
print(selected_name)
print(selected_name.tag_name)
print(selected_name.text)

selected_names=driver.find_element_by_name("query")
print(selected_names)

