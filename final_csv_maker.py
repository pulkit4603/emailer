import csv

# OPTIONAL
# Function to make a csv file of the final teams
def make_teams_csv(users, filename="final_teams.csv"):
    fieldnames = users[0].keys()
    with open(filename, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)