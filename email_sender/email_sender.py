import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Name'
email['to'] = 'email adress'
email['subject'] = 'My python sender'

email.set_content(html.substitute(name='Patryk'), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('email', 'Password')
	smtp.send_message(email)
	print('all good boss!')
