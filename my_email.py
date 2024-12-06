import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, message, recipient, cc=None, bcc=None):
    """
    Send email with the specified subject, message, and recipients.

    parameters:
                subject(string):subject of email
                message(string):body content of Email
                recipients(string): recipients of Email
                cc(list,optional):list of email address show in CC. default is None.
                bcc(list,optional):list of email address show in BCC. default is None.

    Returns:
                str: message that show status of sending email
                    if success send email print "Email send successfull", else show error message.

    """
    sender_email = "sender@gmail.com"
    sender_password = "your password"
    # create Email message
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient
    msg["Subject"] = subject
    # add message body
    msg.attach(MIMEText(message, "plain"))
    # add CC
    if cc:
        msg["Cc"] = ", ".join(cc)
        recipient = [recipient] + cc
    else:
        recipient = [recipient]

    # add BCC
    if bcc:
        recipient += bcc
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587  # for TLS,use port 465 for SSL
        # connect to SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # secure connection
            server.login(sender_email, sender_password)  # login to email account
            server.send_message(
                msg, from_addr=sender_email, to_addrs=recipient
            )  # send message

            print("Email send successfull")
    except Exception as e:
        print(f"Error: {e}")


subject = "test email"
message = "this is test email message"
recipient = "recipient@gmail.com"
send_email(subject, message, recipient)
