import smtplib
from email.mime.text import MIMEText
from tracker.config import EMAIL_ADDRESS, EMAIL_PASSWORD

def send_email(subject, body):
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("📧 Email alert sent")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
