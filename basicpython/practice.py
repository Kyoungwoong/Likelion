import random

snack = ["눈을 감자", "쫄병스낵", "치토스"]
print(random.choice(snack))

info = {"본가": "경기도", "취미": "축구", "mbti":"esfj"}
print(info)
print(info.get("취미"))
print(len(info))
del info["mbti"]
print(info)
info.clear()
print(info)

snack.append("포카칩")
print(snack)
del snack[2]
print(snack)

