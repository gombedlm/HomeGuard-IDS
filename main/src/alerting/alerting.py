class Alerting:
    def __init__(self):
        # Initialize any setup if needed
        pass
    
    def send_email(self, subject, message, recipient):
        # Replace with actual email sending code
        print(f"Email sent to {recipient}: {subject} - {message}")
    
    def send_sms(self, message, recipient):
        # Replace with actual SMS sending code
        print(f"SMS sent to {recipient}: {message}")
    
    def send_notification(self, message):
        # Replace with actual system notification code
        print(f"System notification: {message}")

# Example usage
if __name__ == "__main__":
    alerter = Alerting()
    alerter.send_email("Test Email", "This is a test email message.", "example@example.com")
    alerter.send_sms("This is a test SMS message.", "+1234567890")
    alerter.send_notification("This is a test system notification.")
