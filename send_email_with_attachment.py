#!/usr/bin/env python

# don't forget to enable access for the less secure apps in gmail account, https://myaccount.google.com/lesssecureapps
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

fromaddr = "my gmail"
toaddr = "responer's email"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Hourly KPI report"
body = "This is a report for Ladbrokes Wallet KPI monitoring"
msg.attach(MIMEText(body, 'plain'))
filename = "kpi_report.xls"
attachment = open("/Users/yhrushchynskyi/Downloads/Excel_reports/kpi_report.xls", "rb")

p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(fromaddr, "gmail_password")
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text)
s.quit()