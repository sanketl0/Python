import os
import sys
import time
import schedule
import datetime
import smtplib as sm
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

def send():
    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sanketlodhe9067@gmail.com","ngsafptslxynynux")
    from_ = "sanketlodhe9067@gmail.com"
    to_ = "sanketborhude02@gmail.com"
    message = MIMEMultipart("alternative")
    message['subject']= "New email with attachements"
    message['from']= "sanketlodhe9067@gmail.com"


    filename="data.csv"
    attachment =open(filename,"rb")

    Ret = MIMEBase('application','octect-stream')
    Ret.set_payload((attachment).read())
    encoders.encode_base64(Ret)
    Ret.add_header('content-Disposition',"attachment;filename="+filename)
    message.attach(Ret)

    server.sendmail(from_,to_,message.as_string())
    server.quit()
    print("File has been sent")
    print("current time is:",datetime.datetime.now())


def script_terminator():
    print("done..................................................")
    sys.exit()

def main():

    print("Mail Sending..............")
    try:
        schedule.every(2).seconds.do(send)
        schedule.every(1).minutes.do(script_terminator)


        while(True):
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print("Error:",e)

if __name__ =="__main__":
    main()