import csv, string, random

# Function to get the length of the file
def flen(fpath):
    file = open(fpath)
    fileLen = len(list(csv.reader(file)))
    file.close()
    return fileLen

# Function to scrape the data from the csv file
def scrape(reader, fileLen):
    users_array = []
    for i in range(fileLen-1):
        userdict = {}
        row = next(reader)
        t = i+1
        teamID = str(t) if t > 99 else "0" + str(t) if t > 9 else "00" + str(t)

        password = ''.join(random.choices(string.ascii_letters, k=6))
        player1,player2 = row[3],row[6] # full name
        player1_firstname, player2_firstname = player1.split(" ")[0], player2.split(" ")[0]

        # email for mailing directly to the user
        email = row[1]
        team_type = row[5].split(" ")[0]
        userdict['teamID'] = teamID
        userdict['player1'] = player1_firstname
        userdict['player2'] = player2_firstname if (team_type == "Duo") else ""
        userdict['email'] = email
        userdict['password'] = password
        
        users_array.append(userdict)
    print(users_array)
    return users_array

# Function to prepare the data
def prepare_data(filepath: str):
    fileLen = flen(filepath)
    file = open(filepath)
    reader = csv.reader(file)
    header = next(reader)
    users = scrape(reader, fileLen)
    return users

# print(prepare_data("./sample_participants_data.csv")) # for testing purposes  