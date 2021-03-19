import os
import mimetypes
import smtplib
from email.message import EmailMessage

GMAIL_ADDRESS = os.environ.get('GMAIL_USER')
GMAIL_PASSWORD = os.environ.get('GMAIL_PASS')

#contacts = [GMAIL_ADDRESS, 'another@email.com']
contacts = [GMAIL_ADDRESS]

msg = EmailMessage()
msg['From'] = GMAIL_ADDRESS
msg['To'] = contacts
#msg['Cc'] = 'another@email.com'
#msg['Bcc'] = 'another@email.com'
msg['Subject'] = 'test-subject-pic'
msg.set_content('test-email-body-pic\n Picture attached')

# list of attachments
files = [
    'sample_attachment/iphone12_slogan.png',
    'sample_attachment/tb_by_state.png'
    ]

for ifile in files:
    with open(ifile, 'rb') as f:
        file_data = f.read()
        file_name = f.name

    ctype, encoding = mimetypes.guess_type(ifile)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compressed), so
        # use a generic bag-of-bits type.
        ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)

    msg.add_attachment(
        file_data, 
        maintype = maintype, 
        subtype = subtype,
        filename = file_name
        )

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(GMAIL_ADDRESS, GMAIL_PASSWORD)
    smtp.send_message(msg)