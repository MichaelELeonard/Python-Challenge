import os
import csv

# Initialize variables
Total_Votes = 0

# List for Canidate Name, total Votes Received, Percentage of Vote Received 
Canidate_Info_List = ["Charles Casper Stockham",0,0.0,"Diana DeGette",0,0.0,"Raymon Anthony Doane",0,0.0]
Canidate_Name = ""
Winner_Name = ""


# Function to Calculate Percentage of Vote Received 
def Convert_To_Percent(index):
    Convert_To_Percent = Canidate_Info_List[index] = round(((Canidate_Info_List[index-1]/Total_Votes) * 100), 3)
    return (Convert_To_Percent)


def Who_Won():
    if Canidate_Info_List[1] > (Canidate_Info_List[4]) and (Canidate_Info_List[7]):    
        return Canidate_Info_List[0]
    elif Canidate_Info_List[4] > (Canidate_Info_List[1]) and (Canidate_Info_List[7]):    
        return Canidate_Info_List[3]
    elif Canidate_Info_List[7] > (Canidate_Info_List[1]) and (Canidate_Info_List[4]):    
        return Canidate_Info_List[6]


# Set file path for reader
csvpath = os.path.join ("Week_3/Week_3_Challenge/python-challenge/PyPoll/Resources/election_data.csv")

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Move pointer past header
    csvheader = next(csvfile)
   
    # Looping through CSV file to tabulate data
    for row in csvreader:

        # Increment Months
        Total_Votes += 1

        Canidate_Name = str(row[2])

        # Constituent voted for Charles Casper Stockham
        if Canidate_Name == str(Canidate_Info_List[0]):

            #Increment vote for Charles Casper Stockham
            Canidate_Info_List[1] =  Canidate_Info_List[1] + 1

        # Constituent voted for Diana DeGette
        elif Canidate_Name == str(Canidate_Info_List[3]):

            #Increment vote for Diana DeGette
            Canidate_Info_List[4] =  Canidate_Info_List[4] + 1

        # Constituent voted for Raymon Anthony Doane
        elif Canidate_Name == str(Canidate_Info_List[6]):

            #Increment vote for Raymon Anthony Doane
            Canidate_Info_List[7] =  Canidate_Info_List [7] + 1


# convert total votes for Charles Casper Stockham onto a % for total vote
Canidate_Info_List[2] = Convert_To_Percent(2)

# convert total votes for Diana DeGette onto a % for total vote
Canidate_Info_List[5] = Convert_To_Percent(5)

# convert total votes for Raymon Anthony Doane onto a % for total vote
Canidate_Info_List[8] = Convert_To_Percent(8)

Winner_Name = Who_Won()

       
 # Printing output to Terminal
print("Election Results")
print()
print("----------------------------")
print()
print(f"Total Votes: {Total_Votes}")
print()
print("----------------------------")
print()
print(f"{Canidate_Info_List[0]}: {Canidate_Info_List[2]}%  ({Canidate_Info_List[1]})")
print()
print(f"{Canidate_Info_List[3]}: {Canidate_Info_List[5]}%  ({Canidate_Info_List[4]})")
print()
print(f"{Canidate_Info_List[6]}: {Canidate_Info_List[8]}%  ({Canidate_Info_List[7]})")
print()
print("----------------------------")
print()
print(f"Winner: {Winner_Name}")
print()
print("----------------------------")

# Printing output to Texty file in directory
f = open("Week_3\Week_3_Challenge\python-challenge\PyPoll\Election_Results.txt", "w")
print("Election Results", file = f)
print("", file = f)
print("----------------------------", file = f)
print("", file = f)
print(f"Total Votes: {Total_Votes}", file = f)
print("", file = f)
print("----------------------------", file = f)
print("", file = f)
print(f"{Canidate_Info_List[0]}: {Canidate_Info_List[2]}%  ({Canidate_Info_List[1]})", file = f)
print("", file = f)
print(f"{Canidate_Info_List[3]}: {Canidate_Info_List[5]}%  ({Canidate_Info_List[4]})", file = f)
print("", file = f)
print(f"{Canidate_Info_List[6]}: {Canidate_Info_List[8]}%  ({Canidate_Info_List[7]})", file = f)
print("", file = f)
print("----------------------------", file = f)
print("", file = f)
print(f"Winner: {Winner_Name}", file = f)
print("", file = f)
print("----------------------------", file = f)
f.close()



