import smtplib
import datetime as dt
import pandas
import random
my_email = "amiraliisazadeh2004@gmail.com"
Password = "xxmijbnlmykuypww"
#  Update the birthdays.csv
data = pandas.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")
#  Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
day = now.day
month = now.month
for item in data_list:
    if item["day"] == day and item["month"] == month:
        random_number = random.randint(1, 3)
        print(random_number)
        name = item["name"]
        email = item["email"]
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        with open(f"../Birthday Wisher (Day 32) start/letter_templates/letter_{random_number}.txt", "r") as file:
            birthday_mail = file.read()
            birthday_mail = birthday_mail.replace("[NAME]", name)
        with open(f"../Birthday Wisher (Day 32) start/letter_templates/letter_{random_number}.txt", "w") as file:
            file.write(birthday_mail)
        print(birthday_mail)
        #  Send the letter generated in step 3 to that person's email address.
        message = f"Subject:HAPPY BIRTHDAY!\n\n{birthday_mail}"

        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(user=my_email, password=Password)
        connection.sendmail(from_addr=my_email, to_addrs=email, msg=message)
        connection.close()



