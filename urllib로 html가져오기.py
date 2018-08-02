from urllib.request import urlopen, Request

url="https://www.google.com"


req=Request(url)
page=urlopen(req)

print(page)
print(page.read())
