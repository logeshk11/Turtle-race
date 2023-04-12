import smtplib

my_mail = "logeshlearningpy@gmail.com"
password = "maodtshloduyjshz"

name=["logu", "kum"]

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_mail, password=password)
connection.sendmail(from_addr=my_mail, to_addrs="kumarlogesh96@gmail.com",)
