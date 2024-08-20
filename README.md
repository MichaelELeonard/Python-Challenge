<img src="Pics/Header.png" width="716" height="354">

# Module 3 Challenge - PYTHON-CHALLENGE

##### Link to PyBank Python code - https://github.com/MichaelELeonard/python-challenge/blob/main/PyBank/main.py
##### Link to PyPoll Python code - - https://github.com/MichaelELeonard/python-challenge/blob/main/PyPoll/main.py


## GOAL
For the Module #3 Challenge we were tasked with creating Python code to manage two potential real-world situations involving a banking institution and a small rural town modernizing its election processes. 

### PyBank Project
For the PyBank project we needed the read in data from a .csv file and create code that will determine: <br>
* The total number of months included in the dataset <br>
* The net total amount of "Profit/Losses" over the entire period <br>
* The changes in "Profit/Losses" over the entire period and the average of those changes <br>
* The greatest increase in profits (date and amount) over the entire period <br>
* The greatest decrease in profits (date and amount) over the entire period <br>

### PyBank Results<br>
* Total Months: 86 <br>
* Total: $22564198 <br>
* Average Change: $-8311.11 <br>
* Greatest Increase in Profits: Aug-16 ($1862002) <br>
* Greatest Decrease in Profits: Feb-14 ($-1825558) <br>


### THE PYTHON CODE
For this project I imported the os & csv libraries, the variables were initialized and the file path to the .csv file was established. A FOR loop was utilized to read the data in the file, storing the total number of months to be examined in Total_Months and the Net Total Profit/Losses in Total_Net. A challenging component of this project was to calculate the Profit/Loss interval amounts that then tabulate the average of that change. The Total_Sum_Change_Amount was calculated by taking the current months Profit/Loss amount (Change _Amount) and then subtracting it from the previous months Profit/Loss change amount (Previous_Change_Amout). An exception needed to manage the first month of data as there was not (Previous_Change_Amout) data to compare to, and so one month was removed in the Average_Change calculation to compensate for the first month. Greatest_Increase, Greatest_Increase_Date, Greatest_Decrease, Greatest_Decrease_Date was tracked while looping through the data as they were output variables for this project. Finally, the results were printed out to the Visual Studio Terminal and a text file (Bank_Results.txt. 

### FINANCIAL RESULTS
The python code examined 86 months of data for a net total amount of:  <br>
* Profit/Losses to of $22,564,198. <br>
* The average change between months was $-8311.11. <br>
* The greatest increase in profits occurred on August 16th with an increase of $1,862,002. <br>
* The greatest decrease in profits occurred on February 14th with a decrease of $-1,825,558. <br>
* The Python code executes efficiently, producing results in approximately 2.13 seconds. <br>


### PyPoll Project
For the PyPoll project we needed the read in the initial data from a .csv file and create code that will determine: 
* The total number of votes cast
* A complete list of candidates who received votes
* The percentage of votes each candidate won
* The total number of votes each candidate won
* The winner of the election based on popular vote

### Election Results
* Total Votes: 369711 <br>
* Charles Casper Stockham: 23.049% (85213) <br>
* Diana DeGette: 73.812% (272892) <br>
* Raymon Anthony Doane: 3.139% (11606) <br>
* Winner: Diana DeGette <br>

### RESULTS
The results of PyPoll project showed that 369,711 votes were cast in the election. Charles Casper Stockham received 85,213 votes representing 23.049% of total votes cast. Diana DeGette received 272,892 votes representing 73.812% of total votes cast. Raymon Anthony Doane received 11,606 votes representing 3.139% of total votes cast. Finally, the code determined that Diana DeGette had won the election based off the popular vote totals received by each candidate. The Python code executes efficiently, traversing 369,712 lines of data and producing results in approximately 2.58 seconds.
