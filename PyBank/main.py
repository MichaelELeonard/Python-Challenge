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
csvpath = os.path.join ("Week_3/Week_3_Challenge/python-challenge/PyBank/Resources/budget_data.csv")

# Open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Move pointer past header
    csvheader = next(csvfile)

    for row in csvreader:
        Total_Months += 1
        Total_Net = Total_Net + int(row[1])
        
     #   print(Previous_Change_Amout)
        if Previous_Change_Amout != 0:
            Change_Amount = int(row[1]) - Previous_Change_Amout
            Total_Sum_Change_Amount += Change_Amount
            
        if Change_Amount > Greatest_Increase:
            Greatest_Increase = Change_Amount 
            Greatest_Increase_Date = (row[0])      
        if Change_Amount < Greatest_Decrease:
            Greatest_Decrease = Change_Amount
            Greatest_Decrease_Date = (row[0])

        Previous_Change_Amout = int(row[1])


Average_Change = (Total_Sum_Change_Amount/(Total_Months-1))
Average_Change = round(Average_Change,2)

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