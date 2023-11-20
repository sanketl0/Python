import os 
import time 
import psutil 

import smtplib
import schedule
from urllib.request import urlopen
from sys import *
import urllib.request
from urllib.error import URLError
from email import  encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart  import  MIMEMultipart

def is_connected():
    try:
        urllib.urlopen("www.google.com",timeout=1)
        return True
    except urllib.URLError as err:
        return False
    
def Mail_sender(filename,time):
    try:
        fromaddr = ("sanketlodhe9067.gmail.com","ngsafptslxynynux")
        toaddr = "lodhesanket6666@gmail.com"
        
        msg = MIMEMultipart()
        msg['from'] = fromaddr
        msg['to'] = toloaddr
        body ="""
        Hello %s,
        Welcome to my Project.
        Please find attached document which contains the Log of Running Process.
        Log file is created at : %s
        
        This is auto generated mail.
        
        
        Thanks & Regards
        """ %(toaddr, time)
        
        subject = """ 
        
        Sanket's PC process log generated at : %s
        """%(time)
        
        msg['subject'] = subject
        msg.attach(MIMEText(body,'plain'))
        
        attachement = open(filename,"rb")
        p =MIMEBase('application','octet-stream')
        p.set_payload((attachement).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition',"attachment; filename=%s"%filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(fromaddr,"sanketlodhe9067.gmail.com")
        text = msg.as_string()
        s.sendmail(fromaddr,toaddr,text)
        a.quit()
        print("Log file successfully sent through Mail")
    except Exception as e:
        print("unable to send message",e)
        
def ProcessLog(log_dir="sanketlodhe"):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except Exception as r:
            print(r)
    
    separator = "-"  * 80
    formatted_time = time.strftime("%Y-%m-%d_%H-%M-%S")
    log_path = os.path.join(log_dir,f"sanket_{formatted_time}.log")
    f = open(log_path,"w")
    f.write(separator+ "\n")
    f.write("sanket process logger : "+time.ctime()+"\n")
    f.write(separator+ "\n")
    f.write("\n")
    
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs =['pid','name','username'])
            vms = proc.memory_info().vms/(1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n" % element)
        print("Log file is successfully generated at location %s"%(log_path))
        
        connected = is_connected()
        if connected:
            startTime = time.time()
            Mail_sender(log_path,time.ctime())
            endTime = time.time()
            
            print('Took %s seconds to send mail'%(endTime-startTime))
        else:
            print("there is no internet conncetion")
        
def main():
    
    try:
        schedule.every(1).minutes.do(ProcessLog)
        while True:
            schedule.run_pending()
            time.sleep(1)
            
    except ValueError as e:
        print(e)
        
    except Exception as s:
        print(s)
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    