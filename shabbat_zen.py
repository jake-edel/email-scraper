"""Email scraper"""
import email, imaplib
import os
from pprint import pp
from dotenv import load_dotenv

load_dotenv()

EMAIL_UN = os.getenv("EMAIL")
EMAIL_PW = os.getenv("APP_KEY")

currentWorkingDirectory = os.getcwd()
# print('Current Working Directory: ', currentWorkingDirectory)

# print('os.environ: ', end = ' ')
# pp(dict(os.environ), indent=8)


def details(subject_header):
    return '(FROM "Robert Tarantino" SUBJECT "'+subject_header+'")'

def attachment_download(SUBJECT):
    username = EMAIL_UN
    password = EMAIL_PW
    url = 'imap.gmail.com'
    detach_dir = '.'

    mail_client = imaplib.IMAP4_SSL(url,993)
    mail_client.login(username, password)
    mail_client.select()

    resp, items = mail_client.search(None, SUBJECT)
    # print(resp)
    items = items[0].split()
    # print(items)

    resp, data = mail_client.fetch(items[1], "(RFC822)")
    mail = email.message_from_string(str(data))
    # print(data)
    # print(mail)
    # print(data == mail)
    # print(data[0][1].decode('UTF-8'))
    bp = email.parser.BytesParser()
    msg = bp.parsebytes(data[0][1])
    # help(bfp)
    # bfp.feed(data[0][1])
    # help(msg)
    # print(msg)
    print(str(msg).split("\"")[3])
    # data = msg.walk()
    # print(data)
    # print(type(bp.parsebytes(data[0][1])))
    
    # print(resp)
    # print(data[0])

    # for emailid in items: 
    #     resp, data = mail_client.fetch(emailid, "(RFC822)")
    #     print(data)

attachment_download(details('Shabbat Shalom'))
