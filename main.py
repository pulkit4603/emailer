from mailer import send_email
from data_preparation import prepare_data
from final_csv_maker import make_teams_csv
import time # for sleep

# The download link to the app (not yet available)
app_link = "https://drive.google.com/"

# The csv file path (preferably in the same directory as the main.py file)
filepath = "./sample_participants.csv"

# The sender email and password (preferably an outlook email account)
sender_email = 'sample@outlook.com' # replace with your email
sender_email_password = 'samplepassword123' # replace with your password

final_teams_list = []

# The main function
def main():
    users = prepare_data(filepath)
    for i in range(len(users)):
        user = users[i]
        send_email(user, app_link, sender_email, sender_email_password)
        final_teams_list.append(user) # add the user to the final list
        time.sleep(30) # sleep for 20 seconds to avoid spamming the mail server
    print("All emails sent successfully!")

    # OPTIONAL: Comment the line below to not obtain a CSV of the final teams list
    make_teams_csv(final_teams_list) # make the final teams csv file

if __name__ == "__main__":
    main()