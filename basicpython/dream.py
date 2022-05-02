# print("list")
# total_list =[]
# while True:
#     que = input("질문을 입력해 주세요:")
#     if(que =="q"):
#         break
#     else:
#         total_list.append({"질문": que, "답변": ""})
# print(total_list)
# for i in total_list:
#     # i는 dictionary 형태로 
#     print(i["질문"])
#     answer = input("답변을 입력해주세요 : ")
#     i["답변"]=answer
# print(total_list)

print("dictionary")
total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if question == "q":
        break
    else:
        total_dictionary[question] = ""
print(total_dictionary)
for i in total_dictionary:
    # i는 key값을 반환
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
print(total_dictionary)