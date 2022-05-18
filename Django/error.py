try:
    4/0
except ZeroDivisionError:
    print("0으로 나누면 안돼요")
finally: 
    print("계산 끝")