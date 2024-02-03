from mailer import send_email
import smtplib
import sys
from data_preparation import prepare_data
from final_csv_maker import make_teams_csv
import time # for sleep

# The download link to the app (not yet available)
app_link = "https://drive.google.com/"

# The csv file path (preferably in the same directory as the main.py file)
filepath = "./sample_participants.csv" # replace with your file path

# The sender email and password (preferably an outlook email account)
sender_email = '' # replace with your email
sender_email_password = '' # replace with your password

final_teams_list = []
failed_teams_list = []
# The main function
def main():
    last_sent = 0 # the last sent teamID
    users = prepare_data(filepath)
    for i in range(len(users)):
        if i<int(last_sent): # skip the users that have already been sent the email
            continue
        user = users[i]
        try:
            send_email(user, app_link, sender_email, sender_email_password)
            final_teams_list.append(user) # add the user to the final list
            user['player2'] = user['player2'].split(" ")[-1] # only the name
            user.pop('email') # remove the email field
            last_sent = user['teamID'] # update the last sent teamID
        except smtplib.SMTPDataError as e:
            if 'WASCL UserAction verdict is not None. Actual verdict is suspend' in str(e):
                print(f"SMTPDataError occurred, terminating script: {e}")
                print(f"Last sent teamID: {last_sent}")
                sys.exit(1)  # terminate the script
            else:
                print(f"An unknown error occurred while sending the email to {user['email']}: {e}")
                user['player2'] = user['player2'].split(" ")[-1] # only the name
                user.pop('email') # remove the email field
                failed_teams_list.append(user)
                continue
        except Exception as e:
            print(f"An error occurred while sending the email to {user['email']}: {e}")
            user['player2'] = user['player2'].split(" ")[-1]
            user.pop('email') # remove the email field
            failed_teams_list.append(user)
            continue
        time.sleep(10) # sleep for 10 seconds to avoid spamming the mail server
    print("All emails sent successfully!")

    # OPTIONAL: Comment the line below to not obtain a CSV of the final teams list
    make_teams_csv(final_teams_list) # make the final teams csv file
    make_teams_csv(failed_teams_list, "failed_emails.csv") # make the failed emails csv file

if __name__ == "__main__":
    main()