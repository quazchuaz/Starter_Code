#import dataset
import os
import csv

#provide filepath
csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Read CSV file
with open(csv_path, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')

#Skip header row and set first_row as a variable to be used further below.
    csv_header = next(csvreader)
    first_row = next(csvreader)

# Initialise variables. Set Months_count to 1 and Net_Profit to the first_row value as we will be skipping the first row of data when calculating changes.
# Initialise max and min change to -infinity and infinity respectively so that any change will trigger the 'if' condition below.
# The above is to avoid cases where all changes are either negative or positive (we initially set the values to 0 for min and max).
    Months_count = 1
    Net_Profit = int(first_row[1])
    Profit_Change = 0
    Max_Change = float('-inf')
    Min_Change = float('inf')
    Min_Month = first_row[0]
    Max_Month = first_row [0]
    
    # Set Prev_Change equal to value in row 1 so that row 1 in loop outputs no change.
    Prev_Change = int(first_row[1])

    #Perform a loop to tally the months and net profit values, beginning at 1 and row 1 values respectively. 

    #Set the current change as a variable that updates as we go down the list. This will enable determining the maximum and minimum values via the 'if' function later.

    #Tallying the Current_Change values will allow us to arrive at the 'Profit_Change' for the period. the Prev_Change value updates as we go down the list of values.
    for row in csvreader:
        Months_count += 1
        Net_Profit += int(row[1])
        Current_Change = int(row[1]) - Prev_Change 
        Profit_Change += Current_Change 
        Prev_Change = int(row[1])
        if Current_Change < Min_Change:
            Min_Change = Current_Change
            Min_Month = row[0]
        if Current_Change > Max_Change:
            Max_Change = Current_Change
            Max_Month = row[0]

#Print Outputs
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {Months_count}")
print(f"Total: ${Net_Profit}")
Average_Change = (round(Profit_Change / (Months_count-1),2))
print(f"Average Change ${Average_Change}")
print(f"Greatest Increase in Profits: {Max_Month} $({Max_Change})")
print(f"Greatest Decrease in Profits: {Min_Month} $({Min_Change})")

#Write Text File
with open ('Financialy_Analysis', 'w') as text:
    text.write("Financial Analysis" +"\n")
    text.write("---------------------------\n\n")
    text.write(f"Total Months: {Months_count}" + "\n")
    text.write(f"Total: ${Net_Profit}" +"\n")
    text.write(f"Average Change ${Average_Change}" + "\n")
    text.write(f"Greatest Increase in Profits: {Max_Month} $({Max_Change})" +"\n")
    text.write(f"Greatest Decrease in Profits: {Min_Month} $({Min_Change})" + "\n")