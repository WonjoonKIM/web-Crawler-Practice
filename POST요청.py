import requests as rq
import json

url="http://www.naver.com"

res=rq.get(url, data=json.dumps({"Key1": " value1", "key2": "value2"}))

print(res.url)
