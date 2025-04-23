import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from tkinter import messagebox

def send_email(message,email):
    subject = "Subject: OTP Confirmation for Reset Password"
    body = f"Your OTP is .......{message}"
    host = "smtp.gmail.com"
    port = 465
    user_name = "kushal.limit@gmail.com"  # Email address
    password = "wbsi hlxp hizf xsnz"  # App password

    context = ssl.create_default_context()

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = user_name
    msg['To'] = email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(user_name, password)
            server.sendmail(user_name, email, msg.as_string())
        messagebox.showinfo(title="OTP",message=f"OTP has been sent to {email}")
    except Exception as e:
        print(f"Failed to send OTP: {e}")


if __name__ == "__main__":
    send_email("150904","dronpatel2510@gmail.com")