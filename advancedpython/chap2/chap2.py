import requests
import json #javascript object notation
# API 
# client와 서버 사이에 규약 즉 개발자가 서버에 API 코드를 올리면 client는 그 코드를 가져와서 사용하면 됌
# 누가 API를 사용하고 있는 지, API를 이용해 사용자 차단 기능 
city = "Seoul"
apikey = "309b3c410757630a946d345c9e8f83e3"
language = "kr"
# f.string
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={language}&units=metric"
result = requests.get(api)
# # 날씨를 나타내는 데이터
# print(result.text)

# 원하는 정보만 뽑아오기 json // 데이터를 주고 받을 때 사용하는 포맷
# json 타입으로 변환
data = json.loads(result.text)

# print(type(result.text)) # str
# print(type(data)) # dict

print("json : " , data["weather"])
# 오류! 
# pass print("str : " , result.text["weather"])

# json형태 잘 파악해서 참조하기
# print("날씨는 ",data["weather"][0]["main"],"입니다.")
print(data["name"],"의 날씨입니다.")
print("날씨는 ",data["weather"][0]["description"],"입니다.")
print("현재 온도는 ",data["main"]["temp"],"입니다.")
print("하지만 체감 ",data["main"]["feels_like"],"일 거에요.")
print("최저 기온은 ",data["main"]["temp_min"],"입니다.")
print("최고 기온은 ",data["main"]["temp_max"],"입니다.")
print("습도는 ",data["main"]["humidity"],"입니다.")
print("기압은 ",data["main"]["pressure"],"입니다.")
print("풍향은 ", data["wind"]["deg"],"입니다.")
print("풍속은 ", data["wind"]["speed"],"입니다.")