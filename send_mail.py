import smtplib, ssl

print("Note: For sending email you must have less secure app access enabled in your gmail account security settings.")
print("!Still working on to make this script work with good api instead.")
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "pushpa98108@gmail.com"  # Enter your address
receiver_email = "mayank98108@gmail.com"  # Enter receiver address
password = "!Qwertyuiop09"
message = "testing dkron"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
