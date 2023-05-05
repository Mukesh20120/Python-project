##################### Extra Hard Starting Project ######################
import smtplib
all_data = {
    "name": {},
    "email": {},
    "year": {},
    "month": {},
    "day": {},
}
with open(file="birthdays.csv") as file:
    data = file.readlines()

my_email = "fake84117@gmail.com"
my_pass = "temppassword"

# connect = smtplib.SMTP("smtp.gmail.com")
# connect.starttls()
# connect.login(user=my_email,password=my_pass)
# connect.sendmail(from_addr=my_email, to_addrs=my_email, msg="subject: Happy Birthday\n\n")
# connect.close()
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




