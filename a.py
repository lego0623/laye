# import imapclient
import os 
import email
import imaplib
import configparser
import smtplib
from email.mime.text import MIMEText

last_user = ""

while True:
    imap_obj = imaplib.IMAP4_SSL('imap.gmail.com')
    imap_obj.login('lookatyouremail4@gmail.com', 'ledh0623')
    # 'email_address@example.com boka poki authenticated (Success)'
    imap_obj.select('Inbox')
    result, data = imap_obj.search(None, 'ALL')

    all_email = data[0].split()

    mail = all_email[len(all_email)-1]
    result, data = imap_obj.fetch(mail, '(RFC822)')
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_bytes(raw_email)
    user_email = email.message_from_bytes(raw_email)['From'].replace("=?UTF-8?B?TEFZRV/roIjsnbQ=?= ", "")
    user_email = user_email.replace("<","")
    user_email = user_email.replace(">","")
    print(user_email)
    ########################################################

    if(last_user == user_email):
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()      # say Hello
        smtp.starttls()  # TLS 사용시 필요
        smtp.login('lookatyouremail4@gmail.com', 'ledh0623')
        
        msg = MIMEText('''오 내기를 받아들이다니 이제 재밌겠군...
        일단 첫번째 단서를 줘야겠지??? 일단 첫번째 단서야 알아서 잘 찾길 바래
        W3W, "집어넣다""단련된""연습곡", 위도, 경도
        아 내가 준 프로그램(게임)에 암호 입력해서 단서 얻는건 잊지 마라고~!''')
        msg['Subject'] = '오 내기를 받아들이는 거지? 좋았어'
        msg['To'] = user_email
        smtp.sendmail('lookatyouremail4@gmail.com', user_email, msg.as_string())
        last_user = user_email