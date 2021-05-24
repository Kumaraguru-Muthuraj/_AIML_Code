# EMAIL CODE ADOPTED FROM
# https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail(toEmail, messageBody):
	mail_content = messageBody
	#The mail addresses and password
	sender_address = 'XXXXX@gmail.com'
	sender_pass = 'RRRRRR'
	receiver_address = toEmail
	#Setup the MIME
	message = MIMEMultipart()
	message['From'] = sender_address
	message['To'] = receiver_address
	message['Subject'] = 'Foodie - Top 10 restaurants'   #The subject line

	#The body and the attachments for the mail
	message.attach(MIMEText(mail_content, 'plain'))

	#Create SMTP session for sending the mail
	session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
	session.starttls() #enable security
	session.login(sender_address, sender_pass) #login with mail_id and password
	text = message.as_string()
	session.sendmail(sender_address, receiver_address, text)
	session.quit()
	print('Mail Sent')
	return

def callSendMail(mail_id, body):
	send_mail(mail_id, body)
	return
