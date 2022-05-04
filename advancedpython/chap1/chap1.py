import requests
from bs4 import BeautifulSoup
from datetime import datetime

# # requests가 다운된 경로 출력
# # 모듈 함수를 모아둔 것
# print(requests)


url = "https://www.naver.com"

# return: requests.response
# print(response) => response 200
response = requests.get(url)

# url 출력
print(response.url)
# response에 담긴 내용 출력 
print(response.content)
# response로 받은 text를 출력
print(response.text)
# ISO-8859-1
print(response.encoding)
# 헤더 출력
print(response.headers)
# <bound method Response.json of <Response [200]>>
print(response.json)
# {}
print(response.links)
# True
print(response.ok)
# 200
print(response.status_code)





