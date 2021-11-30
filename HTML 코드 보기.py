import requests as rq

url="https://www.google.com"

res=rq.get(url)

print(res.content)
