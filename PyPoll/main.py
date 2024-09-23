import os
import csv

# Initialize variables
Total_Votes = 0

# List including Canidate Name, total Votes Received, Percentage of Vote Received 
Canidate_Info_List = ["Charles Casper Stockham",0,0.0,"Diana DeGette",0,0.0,"Raymon Anthony Doane",0,0.0]

# Initialize Variables
Canidate_Name = ""
Winner_Name = ""



# Function to calculate percentage of votes received 
def Convert_To_Percent(index):
    Convert_To_Percent = Canidate_Info_List[index] = round(((Canidate_Info_List[index-1]/Total_Votes) * 100), 3)
    return (Convert_To_Percent)



# Function to determine the name of the winner of the election
def Who_Won():
    if Canidate_Info_List[1] > (Canidate_Info_List[4]) and (Canidate_Info_List[7]):    
        return Canidate_Info_List[0]
    elif Canidate_Info_List[4] > (Canidate_Info_List[1]) and (Canidate_Info_List[7]):    
        return Canidate_Info_List[3]
    elif Canidate_Info_List[7] > (Canidate_Info_List[1]) and (Canidate_Info_List[4]):    
        return Canidate_Info_List[6]



# Set file path for reader
csvpath = os.path.join ('Week_3_Challenge/python-challenge/PyPoll/Resources/election_data.csv')    

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Move pointer past header
    csvheader = next(csvfile)
   
    # Looping through CSV file to calculate data
    for row in csvreader:

        # Increment Total_Votes cast in election
        Total_Votes += 1

        # Set the name of the canidate in row being examined
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



# Call Convert_To_Percent function to determine percent of vote received by Charles Casper Stockham
Canidate_Info_List[2] = Convert_To_Percent(2)

# Call Convert_To_Percent function to determine percent of vote received by Diana DeGette
Canidate_Info_List[5] = Convert_To_Percent(5)

# Call Convert_To_Percent function to determine percent of vote received by Raymon Anthony Doane
Canidate_Info_List[8] = Convert_To_Percent(8)

# call Who_Won funcition to determine name of election winner
Winner_Name = Who_Won()


       
 # Printing election results output to Terminal
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

# Printing election results output to Text file in directory
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



