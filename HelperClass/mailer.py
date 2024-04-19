import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests

def send_sms(smsdata):
    try:
        url = smsdata.url
        url = url.replace('#USERNAME#',smsdata.username)
        url = url.replace('#APIKEYVAR#',smsdata.apikey)
        url = url.replace('#SENDERIDVAR#',smsdata.senderid)
        url = url.replace('#SENDNOVAR#',smsdata.receipient)
        url = url.replace('#SENDMSGVAR#',smsdata.message)
        res = requests.get(url)
        return True
    except Exception as e:
        return False

def send_whatsapp(url,whatsappdata):
    try:
        whatsapirequest = {'apikey': whatsappdata.apikey, 'mobile': whatsappdata.mobile,'msg': whatsappdata.msg }
        res = requests.post(url=url, params=whatsapirequest)
        return {'Status': True, 'Message': None, 'ResultData': []}
    except Exception as e:
        return {'Status': False, 'Message': str(e.message), 'ResultData': []}
    
def send_email(emailObj):
    try:
        sender_email = emailObj.frommail
        password = emailObj.password
        smtp_server = emailObj.emailserver
        smtp_port = emailObj.port

        msg = MIMEMultipart()
        msg["Subject"] = emailObj.subject
        msg["From"] = emailObj.frommail 
        msg["To"] = emailObj.tomail
        html_message = emailObj.message

        if html_message:
            # Create an HTML part of the message
            html_part = MIMEText(html_message, "html")
            msg.attach(html_part)

        # Establish a secure SMTP connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.ehlo()
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, emailObj.tomail, msg.as_string())
        return True

    except Exception as e:
        return False
