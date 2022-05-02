from googletrans import Translator

## 실제로 번역을 수행할 객체를 만들기
translator = Translator()

translation = translator.translate("nice to meet you", dest = 'ko')

for trnaslate in translation:
    print(trnaslate.origin + "->" + trnaslate.text)