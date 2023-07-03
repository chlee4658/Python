import smtplib
import os


# 몇 번째 파일을 보낼 지 선택합니다.
f = open("./data/send_num.txt")
num= f.readline()
f.close()
num=int(num)
print(num)

# 파일을 읽어 메일의 메시지를 만듭니다.
f = open("./data/eco_words.csv", encoding="UTF-8")
eco = f.readlines()
f.close()

mail_con = eco[num]
sub, con = mail_con.split(",")
msg = """Subject: {},
{}""".format(sub,con)

# 메일서버에 접속하여, 메일을 발송합니다.
smtp = smtplib.SMTP("smtp.gmail.com", 587)
smtp.starttls()
smtp.login("메일주소를 입력합니다.","비밀번호를 입력합니다.")
smtp.sendmail("보내는 사람 주소를 입력합니다.","받는 사람 주소를 입력합니다.", msg.encode("UTF-8"))
smtp.quit()


# 메일을 발송한 행을 기록합니다
if num >= ( len(eco)-1 ):
    num = 0
else:
    num = num + 1

f = open("./data/send_num.txt", "w")
f.write(str(num))
f.close()

command = "shutdown -s -t 300"
os.system(command)
