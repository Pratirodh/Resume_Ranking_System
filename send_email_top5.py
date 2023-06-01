import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email_top5(to_list):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "khwopamajorproject@gmail.com"
    password = "mtrgrryuysuajjvl"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo() 
        server.starttls(context=context)
        server.ehlo() 
        server.login(sender_email, password)
        for to in to_list:
            message = MIMEMultipart()
            message["Subject"] = "Email test"
            message["From"] = sender_email
            message["To"] = to

            body = """\
            Hello,

            This is the email body.

            Regards,
            Sender
            """
            message.attach(MIMEText(body, "html"))

            try:
                server.sendmail(sender_email, to, message.as_string())
                print("Email sent to", to)
            except Exception as e:
                print(f"Error sending email to {to}: {e}")
        print("All emails sent.")

    return "emails are sent to top5"
