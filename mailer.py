import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback
import csv, string, random

filepath = "./sample_participants_data.csv"


def flen(fpath):
    file = open(fpath)
    fileLen = len(list(csv.reader(file)))
    file.close()
    return fileLen

def scrape(reader, fileLen):
    print(fileLen)
    for i in range(fileLen-1):
        row = next(reader)
        t = i+1
        tid = str(t) if t > 99 else "0" + str(t) if t > 9 else "00" + str(t)
        # print(tid)
        password = ''.join(random.choices(string.ascii_letters, k=6))
        player1,player2 = row[2], row[6] #full name
        p1_f, p2_f = player1.split(" ")[0], player2.split(" ")[0]

        #emailfor mailing directly to the user
        email = row[1]

        print(f"Tid: {tid} \nPlayer1: {p1_f} { 'Player2: ' + p2_f if p2_f != '' else ''} \nEmail: {email} \nPassword: {password}\n")

def send_email(subject, message):
    msg = MIMEMultipart("alternative")
    msg['From'] = 'pulkit.dwivedi.logger@outlook.com'
    msg['To'] = 'pulkitdwivedi123@gmail.com'
    msg['Subject'] = subject

    html_content = """
<html>
  <body>
    <h1>Mailtrap Blog</h1>
    <h3>
      Wassup G,<br /><br />
      What are those? <br />
    </h3>
    <p>
      <a href="https://blog.mailtrap.io/2018/09/27/cloud-or-local-smtp-server"
        >SMTP Server for Testing</a
      >
    </p>
    <p>
      Feel free to <strong>let us</strong> know what content would be useful for
      you!
    </p>
  </body>
</html>
""" 
    
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(msg['From'], 'pulkitdwivedilogger123')
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        error_message = traceback.format_exc()
        print("An error occurred: ", error_message)
        send_email('Your script has crashed', error_message)
