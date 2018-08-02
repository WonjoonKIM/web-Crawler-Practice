import requests as rq

url="http://www.naver.com"

res=rq.get(url, params={"Key1": " value1", "key2": "value2"})

print(res.url)
