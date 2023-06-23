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
    print(f"Header: {csv_header}")