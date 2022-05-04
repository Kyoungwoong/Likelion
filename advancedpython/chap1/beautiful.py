import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "https://www.naver.com"

response = requests.get(url)

# str type
print(type(response.text))
# bs4.BeautifulSoup type
# BeautifulSoup(데이터, 파싱방법)
print(type(BeautifulSoup(response.text, 'html.parser')))

# BeautifulSoup 객체만들기
# html 문자열에 대해서 parsing
soup = BeautifulSoup(response.text,'html.parser')

# 제일 위에 있는 title 태그로 감싸진 부분 
print(soup.title)
# 제일 위에 있는 title 태그로 감싸진 부분 안의 내용물
print(soup.title.string)
# 제일 위에 있는 p
print(soup.p)
# 제일 위에 있는 span
print(soup.span)
# soup안에 모든 span 출력
print(soup.findAll('span'))
# print(soup.span.string) string은 하나에 대한 내용물만 출력가능 findAll('span).string하면 안됌
# 제일 위에 있는 a
print(soup.a)
# a 태그로 감싸진 모든 부분 list형태로 작성 
# 두번째 파라미터 class 
result = soup.findAll('a', 'issue')

# for i in result:
#     print(i.string)
#     #이거 왜 none이 출력됨? 답 -> png파일

cnt = 1
f = open("issueresult.txt", 'a')
# print(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n\n\n"))
f.write(datetime.today().strftime("%Y년 %m월 %d일자 naver 실시간 기사\n"))
for i in result:
    f.write(str(cnt) + ". " + i.get_text()+ "\n")
    cnt += 1
f.close()

# headers 는 사용자가 크롤링 할 수 있도록 해주는 명령어
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
rank = 1
# span - item_title
results = soup.findAll('span','item_title')

