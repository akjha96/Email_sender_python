import smtplib, ssl
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'ABC'
email['to'] = 'abcswe@gmail.com'
email['subject'] = 'Test with python'

email.set_content('This is sent using python!!!' + html.substitute({'name': 'Tin Tin'}), 'html')

# context = ssl.create_default_context()
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('abc@gmail.com', 'abcdef@1234')
    smtp.send_message(email)

print('All Done...')
