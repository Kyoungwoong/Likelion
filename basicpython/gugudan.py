print("구구단을 외자 구구단을 외자!\n")
while 1:
    dan = int(input("몇단을 보실래요?\n "))
    if(dan > 9):
        print("단의 범위를 넘어갔어요\n")

    else:
        for i in range(1,10):
            print(dan, " X " ,i," = " ,dan*i)
            print("")
        break
