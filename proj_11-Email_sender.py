import smtplib

to = input("Enter the email of recipent: \n")
content = input("Enter content for mail : \n")

def send_email(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','password_here')
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()

send_email(to,content)
