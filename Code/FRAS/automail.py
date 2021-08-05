import yagmail
import os
import datetime
date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
body ="Hello"
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
# mail information
yag = yagmail.SMTP("ritikcream8755@gmail.com", "Ritikcream8755**")

# sent the mail
yag.send(
    to="ritikcream8755@gmail.com",
    subject=sub, # email subject
    contents=body,  # email body
    attachments= filename  # file attached
)
print("Email Sent!")
