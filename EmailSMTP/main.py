import smtplib
import datetime as dt

def send_email():
    my_email = input("Enter your email:\n")
    rec_email = input("Enter recipient email:\n")
    pwrd = "buwrzileuxevbowd"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # encryption for security
        connection.login(user=my_email, password=pwrd)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=rec_email,
            msg="Subject:Hello Stam, I am from the future\n")

def datetime_stuff():
    now = dt.datetime.now()
    print(now.month)
    my_birthday = dt.date(year=1995, month=3, day=12)
    print("Stam's birthday: {}".format(my_birthday))

def main():
    datetime_stuff()

if __name__ == '__main__':
    main()

