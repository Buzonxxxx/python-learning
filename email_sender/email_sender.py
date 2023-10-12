# Need to use Gmail app password: 
# Turn on 2-step verification
# Generate app passord here: https://myaccount.google.com/apppasswords)

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'buzonxxxx'
email['to'] = 'buzonliao@gmail.com'
email['subject'] = 'Good morning, here is you daily motivation quote!'

email.set_content(html.substitute({'name': 'Louis'}), 'html')

with open('pw/pw.txt', mode='r') as my_file:
    pw = my_file.read()

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('buzonxxxx@gmail.com', pw)
    smtp.send_message(email)
    print('all good boss!')
