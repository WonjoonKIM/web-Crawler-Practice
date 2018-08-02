import requests as rq

url="https://www.ygosu.com"

res=rq.get(url)

print(res)


cookies=res.cookies

print(dict(cookies))
