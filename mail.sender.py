import os
import os
import sys
import csv
import time
import schedule
import datetime
import smtplib as sm
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def sender():

    server = sm.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("sanketlodhe9067@gmail.com","ngsafptslxynynux")
    from_ = "sanketlodhe9067@gmail.com"
    to_ = "lodhesanket666@gmail.com"
    message = MIMEMultipart("alternative")
    message['subject']= "Something Something"
    message['from']= "sanketlodhe9067@gmail.com"

    msg ='''
          asdfghjhhhhhh \n
          123455
    '''

    text = MIMEText(msg,"plain")
    message.attach(text)
    server.sendmail(from_,to_,message.as_string())
    server.quit()
    
    print("...................MESSAGE HAS BEEN SENT successfully............................")
    print("Task based on minutes get schedule:",datetime.datetime.now())



def main():

    print("Mail send Using script")

    try:
        # it sending msg every minutes
        schedule.every(1).minutes.do(sender)

        #if we want to send specific day like every monday with specific time
        #schedule.every().monday.at("14:00").do(sender)
        
        #it sleep the process for a second
        while(True):
            schedule.run_pending()
            time.sleep(1)

    except Exception as e:
        print("Error: ",e)

if __name__=="__main__":
    main()




