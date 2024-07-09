import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Alerting:
    def __init__(self):
        self.email_address = 'your_email@example.com'
        self.email_password = 'your_email_password'

    def send_email(self, subject, message, recipient_email):
        try:
            msg = MIMEMultipart()
            msg['From'] = self.email_address
            msg['To'] = recipient_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            server = smtplib.SMTP('smtp.example.com', 587)  # Update with your SMTP server details
            server.starttls()
            server.login(self.email_address, self.email_password)
            server.sendmail(self.email_address, recipient_email, msg.as_string())
            server.quit()
            print(f"Email sent successfully to {recipient_email}")
        except Exception as e:
            print(f"Failed to send email: {str(e)}")
