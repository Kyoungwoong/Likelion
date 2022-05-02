import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.naver.com"

response = requests.get(url)

# BeautifulSoup 객체만들기
# html 문자열에 대해서 parsing
soup = BeautifulSoup(response.text,'html.parser')

# # 제일 위에 있는 title 태그로 감싸진 부분
# print(soup.title)
# # 제일 위에 있는 title 태그로 감싸진 부분 안의 내용물
# print(soup.title.string)
# # 제일 위에 있는 p
# print(soup.p)
# # 제일 위에 있는 span
# print(soup.span)
# # 제일 위에 있는 a
# print(soup.a)
# a 태그로 감싸진 모든 부분 list형태로 작성
result = soup.findAll('a', 'issue')

# for i in result:
#     print(i.string)
#     #이거 왜 none이 출력됨?

cnt = 1
f = open("issueresult.txt", 'w')
print(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n\n\n"))
f.write(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n"))
for i in result:
    f.write(str(cnt) + ". " + i.get_text()+ "\n")
    cnt += 1
f.close()