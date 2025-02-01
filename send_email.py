import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465 

    username = "ashwin.bckup@gmail.com"
    password = "zwak iqpl biwe yyqf"

    receiver_email = "nmashwin145@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)
        server.quit()