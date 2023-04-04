import os
import smtplib   
from email import encoders
from email.mime.base import MIMEBase 
from email.mime.image import MIMEImage  
import mimetypes 

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText      

import Moduls.work_ini as work_ini


def get_addr_from():
    return work_ini.get_email_from()

def get_addr_from_pass():
    return work_ini.get_pass_email_from()

def get_addr_to():
    return work_ini.get_email_to()


def get_file(filepath):
    filename = os.path.basename(filepath)  

    ctype, encoding = mimetypes.guess_type(filepath) 
    maintype, subtype = ctype.split('/', 1)

    with open(filepath, 'rb') as fp:
            file = MIMEBase(maintype, subtype)        
            file.set_payload(fp.read())        
            fp.close()
    encoders.encode_base64(file)       
    file.add_header('Content-Disposition', 'attachment', filename=filename)
    
    return file     


def start(rep_title, link_arch=None, link_disk=None):
    # addr_from = 'stestpython5mtp482@yandex.ru'
    # addr_to   = 'artemzolobov24@gmail.com'       
    # password  = 'Qaz2584561297'       
    
    addr_from = get_addr_from()
    addr_to = get_addr_to()
    password = get_addr_from_pass()     

    msg = MIMEMultipart()                        
    msg['From']    = addr_from                       
    msg['To']      = addr_to                         
    msg['Subject'] = str(rep_title).title()     

    
    if link_disk:
        body = str(rep_title).capitalize() \
            + "\n\nСсылка на файл(Яндекс Диск)\n\n"
        
        body += link_disk
        msg.attach(MIMEText(body, 'plain'))     
        
    
    if link_arch:
        body = str(rep_title).capitalize()
        msg.attach(get_file(link_arch))    
        msg.attach(MIMEText(body, 'plain'))               
    
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)           
    server.login(addr_from, password)       
    server.send_message(msg)                   
    server.quit()                             