import smtplib as root
from email import message
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail():
    login = raw_input('Vvedite vashy pochty')
    password = raw_input('vvedite porol')
    url = raw_input('URL:')
    toaddr = raw_input('komy')
    topic = raw_input('tema')
    massege = raw_input('vvedite soobschenie:')

    msg = MIMEMultipart()

    msg['Subject'] = topic
    msg['From'] = login
    body = message
    msg.attach(MIMEText(body, 'plain'))

    server = root.SMTP_SSL(url, 465)
    server.login(login, password)
    server.sendmail(login, toaddr, msg.as_string())


def send_main():
    pass


def main():
    send_main()


if __name__ == '__main__':
    main()

