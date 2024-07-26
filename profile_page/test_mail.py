from django.core.mail import send_mail

subject = 'Test Email'
message = 'This is a test email sent using SMTP in Django'
from_email = 'mar.ayoub98@gmail.com'
recipient_list = ['mariam.ayoub13@yahoo.co.uk']

send_mail(subject, message, from_email, recipient_list)