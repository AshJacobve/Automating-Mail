from Google import create_service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import openpyxl


# Authorization
CLIENT_SECRET_FILE='credentialss.json'
API_NAME='gmail'
API_VERSION='v1'
SCOPES=['https://mail.google.com/']


# load excel with its path
wrkbk = openpyxl.load_workbook("CompContact.xlsx")

sh = wrkbk.active

# iterate through excel and display data
for row in sh.iter_rows(min_row=2, min_col=1, max_col=2):
    count=1
    for cell in row:
        if count==1:
            company=cell.value
            company=company.rstrip()
            print("Company is:", company)
            count+=1
        if count==2:
            email=cell.value
    print("Email Id is:", email)
    Mess=''
    file_object=open("Mail.txt", 'r')
    for char in file_object.read():
        if char=='{':
            Mess+=company
        else:
            Mess+=char

    #   Message Forwarding
    service= create_service(CLIENT_SECRET_FILE, API_NAME, API_VERSION,SCOPES)
    emailMsg = str(Mess)
    mimeMessage = MIMEMultipart()
    mimeMessage['to'] = str(email)
    mimeMessage['subject']= 'Internship Application - Ashwin Jacob'
    mimeMessage.attach(MIMEText(emailMsg, 'plain'))
    raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

    message= service.users().messages().send(userId='',body={'raw':raw_string}).execute()
    print("E-mail sent successfully\n\n\n")