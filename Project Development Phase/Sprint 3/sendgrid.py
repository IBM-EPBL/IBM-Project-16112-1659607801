import smtplib
import sendgrid
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "Interview Call"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    print("sorry we cant process your candidature")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("ranush.krishna@gmail.com", "VsS6tLfzAyq5@Md12")
    message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("ranush.krishna@gmail.com", email, message)
    s.quit()
def sendgridmail(user,TEXT):
    sg = sendgrid.SendGridAPIClient('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')#////////////////////////////////
    from_email = Email("ranush.krishna@gmail.com")  # Change to your verified sender
    to_email = To(user)  # Change to your recipient
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()
    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)
    


#--------------------------------------------------------------------------------

message = Mail(
    from_email='ranush.krishna@gmail.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content="")
try:
    sg = SendGridAPIClient(os.environ.get('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'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)