print("나이 데이터 베이스에 오신 걸 환영합니다.")

dic = {"kim": 15}
while 1:
    case = int(input("어떤 작업을 수행하시겠습니까? 1)생성하기 2)목록보기 3)수정하기 4)삭제하기 5)프로그램 끝내기: "))
    if(case == 5):
        print("수고하셨습니다!!!")
        break

    elif(case == 1):
        key = input("이름을 입력 해 주세요: ")
        age = int(input("나이를 입력 해 주세요: "))
        while age < 0:
            print("나이를 잘못 입력하셨습니다.")
            age = int(input("나이를 양수로 입력 해 주세요: "))
        dic[key] = age
    
    elif(case == 2):
        print("-----나의 데이터 베이스-------")
        for i in dic:
            print(i, ":", dic[i])
        print("-------------------------")
    
    elif(case == 3):
        Mod_key = input("나이를 수정할 이름을 적어주세요: ")
        Mod_age = int(input("수정할 나이를 적어주세요: "))
        while dic.get(Mod_key) == None: 
            print("해당 이름은 없습니다.")
            Mod_key = input("이름을 바르게 입력해주세요: ")
        dic[Mod_key] = Mod_age
    
    elif(case == 4):
        Del_key = input("나이를 삭제할 이름을 적어주세요: ")
        del dic[Del_key]
f.close()