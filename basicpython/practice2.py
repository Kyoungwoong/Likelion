# for x in range(30):
#     print(x)

# foods = ["된장찌개", "피자", "제육볶음"]

# for x in range(3):
#     print(foods[x])
# print()
# for x in foods:
#     print(x)

# info = {"고향":"서울", "취미":"축구","좋아하는 음식":"케이크"}
# for x,y in info.items():
#     print(x + y)

# foods_set1 = set(foods)
# foods_set2 = set(["된장찌개", "피자", "제육볶음"])
# print(foods_set1)
# print(foods_set2)

# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 | menu2 합집합
# menu3 = menu1 & menu2 교집합
# menu3 = menu1 - menu2 차집합
# print(menu3)

# import random
# food = random.choice(["된장찌개", "피자", "제육볶음"])

# if(food =="제육볶음"):
#     print("곱배기 주세요")
# else:
#     print("그냥 주세요")
# print("종료")
set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"
# print(set_lunch - set(list(item))) "짜". "장","면"
print(set_lunch - set([item]))
print(set_lunch)