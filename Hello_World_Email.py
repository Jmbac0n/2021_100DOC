import smtplib

switch = True

# Sender Email Credentials
gmail_user = ''
gmail_password = ''

# Email Properties
sent_from = gmail_user
to = ['']
email_text = ("""\
Subject: 2021\n
Hello World!
    
""")

# Conditions

if switch == True:
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email Sent')
    except Exception as e:
        print(e)
        print('Email failed to send')
else:
    print("Nope")