import csv

# OPTIONAL
# Function to make a csv file of the final teams
def make_teams_csv(users):
    fieldnames = users[0].keys()
    with open('final_teams.csv', mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)