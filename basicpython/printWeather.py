def printWeather(wdict, w):
    print(w,"에 맞는 옷은 " ,wdict[w][0],"입니다")
    print(w,"의 제철 과일은 " ,wdict[w][1],"입니다")
    

wdict = {"봄": ["코트", "딸기"],
        "여름": ["반팔", "수박"],
        "가을": ["긴팔", "사과"],
        "겨울": ["패딩", "감귤"]}

w = input("현재 계절은 어느 계절인가요? - 봄, 여름, 가을, 겨울: ")

printWeather(wdict,w)