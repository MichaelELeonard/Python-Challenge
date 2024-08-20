import os
import csv

# Initialize variables
Total_Months = 0
Total_Net = 0
Change_Amount = 0
Previous_Change_Amout = 0
Total_Sum_Change_Amount = 0
Average_Change = 0.0
Greatest_Increase = 0
Greatest_Decrease = 0
Greatest_Increase_Date = ""
Greatest_Decrease_Date = ""

# Set file path for reader
csvpath = os.path.join("budget_data.csv")
 
# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Move pointer past header
    csvheader = next(csvfile)

    # Looping through CSV file
    for row in csvreader:

        #Increment Months
        Total_Months += 1

        # Add amount to total_Net
        Total_Net = Total_Net + int(row[1])
        
        # Skip first line of data because there is no Previous_Change_Amout information (first month))
        if Previous_Change_Amout != 0:
            Change_Amount = int(row[1]) - Previous_Change_Amout
            Total_Sum_Change_Amount += Change_Amount

        # Check to see if Change_Amount is the Greatest_Increase so far, if so set to Greatest_Increase   
        if Change_Amount > Greatest_Increase:
            Greatest_Increase = Change_Amount 
            Greatest_Increase_Date = (row[0])     

        # Check to see if Change_Amount is the Greatest_Decrease so far, if so set to Greatest_Decrease        
        if Change_Amount < Greatest_Decrease:
            Greatest_Decrease = Change_Amount
            Greatest_Decrease_Date = (row[0])

        # Track Previous_Change_Amout for Change_amount calculation in line #37
        Previous_Change_Amout = int(row[1])

# Calculating the Average_Change. Total_Months-1 used to compensate for no change in the first month as there is no previous months data for calculation
# Rounding to two decimal places 
Average_Change = round((Total_Sum_Change_Amount/(Total_Months-1)), 2)


# Printing output to Terminal
print("Financial Analysis")
print()
print("----------------------------")
print()
print(f"Total Months: {Total_Months}")
print()
print(f"Total: ${Total_Net}")
print()
print(f"Average Change: $ {Average_Change}")
print()
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})")
print()
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})")

# Printing output to Text file in directory
f = open("Week_3\Week_3_Challenge\python-challenge\PyBank\Bank_Results.txt", "w")
print("Financial Analysis", file = f)
print("", file = f)
print("----------------------------", file = f)
print("", file = f)
print(f"Total Months: {Total_Months}", file = f)
print("", file = f)
print(f"Total: ${Total_Net}", file = f)
print("", file = f)
print(f"Average Change: $ {Average_Change}", file = f)
print("", file = f)
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${Greatest_Increase})", file = f)
print("", file = f)
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${Greatest_Decrease})", file = f)
f.close()