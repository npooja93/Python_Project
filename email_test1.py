# Python code to illustrate Sending mail with attachments
# from your Gmail account 
  
# libraries to be imported
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image,ImageTk

fromaddr = "epscmu698@gmail.com"
def send_Email(toEmail_ID,qr_file_name,trip_id):
    try:
        msg = MIMEMultipart()
        msg['From'] = fromaddr    
        msg['To'] = toEmail_ID
        msg['Subject'] = f"Elite Parking Booking - Trip ID : {trip_id}"
        body = f"Elite Parking Booking - Trip ID : {trip_id}"
        print(f"Email - {msg['To']}")
        msg.attach(MIMEText(body, 'plain'))
        #filename = f"data/{qr_file_name}.png"
        attachment = open(qr_file_name, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename= {qr_file_name}.png")
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "ppkkfjntahoxwumm")
        text = msg.as_string()
        s.sendmail(fromaddr, toEmail_ID, text)
        s.quit()
        return 0
    except:
        raise Exception("Cannot send the email")
        return 1
    