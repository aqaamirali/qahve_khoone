########################## send_email_testing ##############################
# import smtplib
#
# my_email = "amiraliisazadeh2004@gmail.com"
# Password = "xxmijbnlmykuypww"
#
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=Password)
# connection.sendmail(from_addr=my_email,
#                     to_addrs="isazadeh2004@gmail.com",
#                     msg="Subject:Hello\n\nsey hello to my little friend")
# connection.close()

############################ date_time_testing #############################
# import datetime as dt
# now = dt.datetime.now()
# print(now)

############################ motivation_saturday_mail_program #############
import datetime as dt
import random
import smtplib

quotes_list = []

# check the day of week
today = dt.datetime.now()
if today.weekday() == 3:
    # make the list of quotes
    with open("quotes.txt", "r") as data:
        # i could use readlines() method it is easier to use but top is more clean
        data_file = data.read()
        quotes_list.append(data_file)
        quotes_list = quotes_list[0].split("\n")
    # pick a random quote
    random_quote = random.choice(quotes_list)

    my_email = "amiraliisazadeh2004@gmail.com"
    Password = "xxmijbnlmykuypww"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=Password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="isazadeh2004@gmail.com",
                        msg=f"Subject:You should read this\n\n{random_quote}")
    connection.close()