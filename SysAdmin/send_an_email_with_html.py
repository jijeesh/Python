# smtplib module send mail
import csv
from tabulate import tabulate
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMETex
import smtplib

text = """
Hello, Friend.

Here is your data:

{table}

Regards,

Me"""

html = """
<html><body><style> 
 table, th, td {{ border: 1px solid black; border-collapse: collapse; }}
  th, td {{ padding: 5px; }}
</style>
</head>
<p>Hello, Friend.</p>
<p>Here is your data:</p>
{table}
<p>Regards,</p>
<p>Me</p>
</body></html>
"""

TO = 'recipient@mailservice.com'
SUBJECT = 'TEST MAIL'
TEXT = 'Here is a message from python.'

with open('input.csv') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

text = text.format(table=tabulate(data, headers="firstrow", tablefmt="grid"))
html = html.format(table=tabulate(data, headers="firstrow", tablefmt="html"))

message = MIMEMultipart(
    "alternative", None, [MIMEText(text), MIMEText(html,'html')])

# Gmail Sign In
gmail_sender = 'sender@gmail.com'
gmail_passwd = 'password'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(gmail_sender, gmail_passwd)



try:
    server.sendmail(gmail_sender, TO.split(","), message.as_string())
    print ('email sent')
except:
    print ('error sending mail')

server.quit()
