from selenium import webdriver

url="https://pjt3591oo.github.io/search"

driver=webdriver.Chrome('chromedriver')
driver.get(url)

driver.execute_script('alert("test")')

for i in range(0, 100):
    print(i)
    # 스크립트는 이 동작을 알 수 없
