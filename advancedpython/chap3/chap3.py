# 모듈을 묶은 큰 단위 library
from googletrans import Translator


# 실제로 번역을 수행할 객체를 만들기
translator = Translator()
# print(Translator)

# sentence = "안녕하세요 코드라이언입니다."
sentence = input("번역을 원하는 문장을 입력하세요 : ")
# detected = translator.detect(sentence)
# print(detected.lang)

# result = translator.translate(sentence, dest="en")

dest = input("어떤 언어로 번역을 원하시나요? ")
result = translator.translate(sentence,dest)
detected = translator.detect(sentence)


print("\n============= 번역 결과 =============\n")
print(detected.lang,":", result.origin)
print(result.dest,":", result.text)
print("\n======================================\n")

