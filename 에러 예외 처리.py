import requests as rq
import time

url="https://www.naver.com"
delay_time=1

def connection(u):
    return rq.get(u)

try:
    connection(url)
    
except rq.exceptions.HTTPError:
    print("HTTP 에러 발생")
except rq.exceptions.Timeout:
    time.sleep(delay_time)
    conncetion(url)
    print("timeout 에러 발생")
except rq.exceptions.MissingSchema:
    print("missing schema 에러 발생")

    
    
