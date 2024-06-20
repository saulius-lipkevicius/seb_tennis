import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email(sender_email, receiver_email, password, subject, log_file):
    # Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Read the log file content
    try:
        with open(log_file, 'r') as file:
            log_content = file.read()
    except FileNotFoundError:
        log_content = 'Log file not found.'

    # Email content
    dabartinis_laikas = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f'Log information as of {dabartinis_laikas}:\n\n{log_content}'
    message.attach(MIMEText(body, 'plain'))

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login to the email account
        server.login(sender_email, password)

        # Send the email
        text = message.as_string()
        server.sendmail(sender_email, receiver_email, text)

        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')
    finally:
        # Close the SMTP server connection
        server.quit()