# SMTP Simple Message Transfer protocol
# IMAP 서버에서 클라이언트로 메일 보내주기
import smtplib
from email.message import EmailMessage
import imghdr
import re

# SMTP 메일 서버를 연결하기
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    # <re.Match object; span=(0, 26), match='codelion.example@gmail.com'> 
    # None  => error
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


# SMTP 메일 서버로 메일 보내기
# SMTP는 MIME형태만 이해할 수 있음
message = EmailMessage()

message.set_content("코드라이언 수업 중입니다.") # content
message["Subject"]= "이것은 제목입니다" # Title
message["From"] = "####@gmail.com" # 보내는 이
message["TO"] = "######@gmail.com" # 받는 이

with open("house.png", "rb")  as image:
    image_file = image.read()
# 동적으로 타입 확인
image_type = imghdr.what('house', image_file)
message.add_attachment(image_file, maintype = "image", subtype = image_type)

# gmail은 SSL을 포함해야함
smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
# # <smtplib.SMTP_SSL object at 0x7fa1952618b0>
# print(smtp)

# SMTP 메일 서버를 로그인하기
# Gmail의 경우 애플리케이션 비밀번호 따로 관리. 새로 생성이 필요
smtp.login("####@gmail.com","########")
sendEmail("####@gmail.com")

# # binary로 표현
# print(image.read())

smtp.quit()

# 정규표현식 
# ^시작 $ 끝
# []하나의 문자, +가 있으면 1회이상 반복
# \. 그 뒤에 .이 붙는다
# {2,3} 최소 2회 최대 3회 반복된다.


