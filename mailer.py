import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback # for error handling

# Function to send the email
def send_email(user: dict, app_link: str, sender_email: str, sender_email_password: str, server_username=None, server_password=None):
    user["player2"] = (" & " + user["player2"]) if (user["player2"] != "") else "" # for duo/solo teams to avoid empty string

    # Email subject
    subject = "TechRace 2024 - Team Login Details"
    # Plain text version of the email
    message = f"""Hello {user['player1']}{user['player2']},
    
    We hope you are as hyped for TechRace as we are! TechRace is an exciting clue-hunt across all of Mumbai which is powered by the TechRace App.
    Clues, points, hints and power-ups can be accessed and bought directly through the app.
    
    Below is the download link for the TechRace 2024 App:
    (go to https://play.google.com/store/apps/details?id=com.oculus.techrace) to download the Android app)
    (go to https://testflight.apple.com/join/9hFC6TqL) to download the iOS app)
    Team Code: {user['teamID']}
    Password: {user['password']}
    Players: {user['player1']}{user['player2']}
    """

    # Email body
    msg = MIMEMultipart("alternative")
    msg['From'] = sender_email
    msg['To'] = f'{user["email"]}'
    msg['Subject'] = subject

    # HTML version of the email
    html_content = f"""
<!DOCTYPE PUBLIC “-//W3C//DTD XHTML 1.0 Transitional//EN” “https://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd”>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1.0" />
    <title></title>
    <style></style>
  </head>
  <body>
    <table
      border="0"
      cellpadding="0"
      cellspacing="0"
      width="100%; color: #ffffff;"
    >
      <tbody>
        <tr>
          <td align="center" bgcolor="rgb(1, 5, 18)" style="color: #ffffff">
            <table
              border="0"
              cellpadding="0"
              cellspacing="0"
              width="100%"
              style="max-width: 600px"
            >
              <tbody>
                <tr>
                  <td align="center" valign="top" style="padding: 36px 24px">
                    <img
                        src="https://i.ibb.co/6Zc8n0F/oculus.png"
                        alt="oculus"
                        border="0"
                        width="48"
                        style="
                          display: block;
                          width: 48px;
                          max-width: 48px;
                          min-width: 48px;
                        "
                        class="CToWUd"
                        data-bit="iit"
                    />
                  </td>
                  <td align="center" valign="top" style="padding: 36px 24px">
                    
                      <img
                        src="https://i.ibb.co/86qm54G/unnamed.png"
                        alt="TechRace 2023 Logo"
                        border="0"
                        width="48"
                        style="
                          display: block;
                          width: 48px;
                          max-width: 48px;
                          min-width: 48px;
                        "
                        class="CToWUd"
                        data-bit="iit"
                      />
                    
                  </td>
                  <td align="center" valign="top" style="padding: 36px 24px">
                    
                      <img
                        src="https://i.ibb.co/3fwrn5T/spit.png"
                        alt="S.P.I.T Logo"
                        border="0"
                        width="48"
                        style="
                          display: block;
                          width: 48px;
                          max-width: 48px;
                          min-width: 48px;
                        "
                        class="CToWUd"
                        data-bit="iit"
                      />
                    
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>

        <tr>
          <td align="center" bgcolor="rgb(1, 5, 18)">
            <table
              border="0"
              cellpadding="0"
              cellspacing="0"
              width="100%"
              style="max-width: 600px"
            >
              <tbody>
                <tr>
                  <td
                    align="left"
                    bgcolor="#0B1120"
                    style="
                      padding: 36px 24px 0;
                      font-family: 'Source Sans Pro', Helvetica, Arial,
                        sans-serif;
                      border-top: 3px solid #7719bf;
                    "
                  >
                    <h1
                      style="
                        margin: 0;
                        font-size: 32px;
                        font-weight: 700;
                        letter-spacing: -1px;
                        line-height: 48px;
                        text-align: center;
                        color: #ffffff;
                      "
                    >
                      The Race Begins Soon
                    </h1>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>

        <tr>
          <td align="center" bgcolor="rgb(1, 5, 18)">
            <table
              border="0"
              cellpadding="0"
              cellspacing="0"
              width="100%"
              style="max-width: 600px"
            >
              <tbody>
                <tr>
                  <td
                    align="center"
                    bgcolor="#0B1120"
                    style="
                      padding: 24px;
                      font-family: 'Source Sans Pro', Helvetica, Arial,
                        sans-serif;
                      font-size: 16px;
                      line-height: 24px;
                    "
                  >
                    <p style="margin: 0; color: #ffffff">
                      <b>Hola Racers!</b><br />
                      We hope you are as hyped for TechRace as we are! TechRace
                      is an exciting clue-hunt across all of Mumbai which is
                      powered by the TechRace App. Clues, points, hints and
                      power-ups can be accessed and bought directly through the
                      app.<br />
                      (<a
                        href="https://play.google.com/store/apps/details?id=com.oculus.techrace"
                        rel="noreferrer"
                        target="_blank"
                        data-saferedirecturl="https://play.google.com/store/apps/details?id=com.oculus.techrace"
                        jslog="32272; 1:WyIjdGhyZWFkLWY6MTc4OTA3NDI4MTAxNTYyNjE2MyJd; 4:WyIjbXNnLWY6MTc4OTA3NDI4MTAxNTYyNjE2MyJd"
                        >click here</a
                      >
                      to download the Android app)
                      <br />
                      (<a
                        href="https://testflight.apple.com/join/9hFC6TqL"
                        rel="noreferrer"
                        target="_blank"
                        data-saferedirecturl="https://testflight.apple.com/join/9hFC6TqL"
                        jslog="32272; 1:WyIjdGhyZWFkLWY6MTc4OTA3NDI4MTAxNTYyNjE2MyJd; 4:WyIjbXNnLWY6MTc4OTA3NDI4MTAxNTYyNjE2MyJd"
                        >click here</a
                      >
                      to download the iOS app)
                      <br />
                      Below are your team's login details for the TechRace 2024
                      App. Please keep them safe and handy.<br />
                    </p>
                    <table
                      border="0"
                      cellpadding="0"
                      cellspacing="0"
                      width="100%"
                      style="max-width: 600px"
                    >
                      <tbody>
                        <tr>
                          <td
                            align="center"
                            bgcolor="#0B1120"
                            style="padding: 36px 24px 0"
                          >
                            <b style="color: #7719bf">Team Code</b><br />
                            <span style="font-size: 24px; color: #ffffff">
                              {user["teamID"]}
                            </span>
                          </td>
                          <td
                            align="center"
                            bgcolor="#0B1120"
                            style="padding: 36px 24px 0"
                          >
                            <b style="color: #7719bf">Password</b><br />
                            <span style="font-size: 24px; color: #ffffff">
                              {user["password"]}
                            </span>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                    <br />
                    <b style="color: #7719bf">Players</b><br />
                    <span style="font-size: 18px; color: #ffffff">
                      {user["player1"]}{user["player2"]}
                    </span>
                    <br />
                    <span style="font-size: 18px; color: #ffffff"></span>
                    <p></p>
                  </td>
                </tr>

                <tr>
                  <td
                    align="center"
                    bgcolor="#0B1120"
                    style="
                      padding: 24px;
                      font-family: 'Source Sans Pro', Helvetica, Arial,
                        sans-serif;
                      font-size: 16px;
                      line-height: 24px;
                    "
                  >
                    <p style="margin: 0; color: #ffffff">
                      Note that your team's password is secret and should not be
                      shared with anyone.<br /><br />
                      We are excited to see your team on 4th February! Please
                      report at 7:30 AM at Sardar Patel Institute of
                      Technology.<br />
                      Any further details will be communicated through the
                      WhatsApp group.
                    </p>
                  </td>
                </tr>

                <tr>
                  <td
                    align="center"
                    bgcolor="#0B1120"
                    style="
                      padding: 24px;
                      font-family: 'Source Sans Pro', Helvetica, Arial,
                        sans-serif;
                      font-size: 16px;
                      line-height: 24px;
                      border-bottom: 3px solid #121826;
                    "
                  >
                    <p style="margin: 0; color: #ffffff">
                      Cheers,<br />
                      Team TechRace 2024

                      <br /><br /><br />
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>

        <tr>
          <td align="center" bgcolor="rgb(1, 5, 18)" style="padding: 24px">
            <table
              border="0"
              cellpadding="0"
              cellspacing="0"
              width="100%"
              style="max-width: 600px"
            >
              <tbody>
                <tr>
                  <td
                    align="center"
                    bgcolor="rgb(1, 5, 18)"
                    style="
                      padding: 12px 24px;
                      font-family: 'Source Sans Pro', Helvetica, Arial,
                        sans-serif;
                      font-size: 14px;
                      line-height: 20px;
                      color: #666;
                    "
                  >
                    <p style="margin: 0; font-weight: bold">
                      Doubts or issues? Message us!
                    </p>

                    <p style="margin: 2px 0">
                      Pulkit Gupta:
                      <a
                        href="tel:+918879911940"
                        rel="noreferrer"
                        target="_blank"
                        >+91 88799 11940</a
                      >
                    </p>
                    <p style="margin: 2px 0">
                      Pulkit Dwivedi:
                      <a
                        href="tel:+917718965798"
                        rel="noreferrer"
                        target="_blank"
                        >+91 77189 65798</a
                      >
                    </p>
                  </td>
                </tr>
              </tbody>
            </table>
          </td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
"""
    # Attach the plain text and HTML version of the email
    msg.attach(MIMEText(message, 'plain'))
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls() # for outlook
        server.login(msg['From'], sender_email_password) # for outlook
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()
        print("Email sent successfully")
    except smtplib.SMTPDataError as e:
        if 'WASCL UserAction verdict is not None. Actual verdict is suspend' in str(e):
            print(f"SMTPDataError occurred, re-raising exception: {e}")
            raise  # re-raise the exception
        else:
            print(f"An error occurred while sending the email to {user['email']}: {e}")
            raise Exception("An unknown error occurred while sending the email")
    except Exception as e:
        error_message = traceback.format_exc()
        raise Exception(error_message)
        print("An error occurred: ", error_message)