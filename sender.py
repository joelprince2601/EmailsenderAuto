import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path=None):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Add attachment if provided
    if attachment_path:
        attachment = open(attachment_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_path)
        message.attach(part)

    # Log in to the server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)

    # Send email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Quit server
    server.quit()

# Example usage:
if __name__ == "__main__":
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"
    receiver_email = "recipient_email@example.com"
    subject = "Test Email"
    body = "This is a test email sent using Python."
    attachment_path = "example_attachment.txt"  # Path to attachment, if any

    send_email(sender_email, sender_password, receiver_email, subject, body, attachment_path)
