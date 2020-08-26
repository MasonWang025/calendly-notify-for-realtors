import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def send(send_config):
    # extract from send_config
    from_address = send_config["from_address"]
    password = send_config["password"]
    from_name = send_config["from_name"]
    subject = send_config["subject"]
    dest_address = send_config["dest_address"]
    html_content = send_config["html_content"]
    opened_attachment = send_config["opened_attachment"]
    attachment_name = send_config["attachment_name"]

    # connect to server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    server.login(from_address, password)

    # message
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = from_name
    msg['To'] = dest_address

    # plain text can also be sent with "text" instead of "html"
    msg.attach(MIMEText(html_content, 'html'))

    # email attachment
    if send_config["opened_attachement"]:
        attachment = open(opened_attachment, "rb")
        p = MIMEBase("application", "octet-stream")  # payload object
        p.set_payload(attachment.read())

        encoders.encode_base64(p)
        p.add_header("Content-Disposition", "attachment; filename=" + attachment_name)
        msg.attach(p)

    # send mail
    text = msg.as_string()
    server.sendmail(from_address, dest_address, text)
