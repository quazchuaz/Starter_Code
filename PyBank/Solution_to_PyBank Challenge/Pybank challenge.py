#import dataset
import os
import csv

#provide filepath
csv_path = os.path.join('..', 'Resources', 'budget_data.csv')

#Read CSV file
with open(csv_path, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
#Skip Header Row
    csv_header = next(csvreader)
    first_row = next(csvreader)

# Define list variable to tally months and net profit, set base values to 0
    Months_count = 1
    Net_Profit = int(first_row[1])
    Profit_Change = 0
    Max_Change = 0
    Min_Change = 0
    Min_Month = first_row[0]
    Max_Month = first_row [0]
    
    # set prev_change equal to value in row 1 so that row 1 in loop outputs no change
    Prev_Change = int(first_row[1])

    #append to expand the relevant lists with the relevant data - months in column 0 and rows in column 1
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

print(Months_count)
print(Net_Profit)
print(round(Profit_Change / (Months_count-1),2))
print(f"{Min_Change} {Min_Month}")
print(f"{Max_Change} {Max_Month}")







