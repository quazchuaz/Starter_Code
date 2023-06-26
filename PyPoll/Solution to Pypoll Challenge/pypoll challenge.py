#Import dataset
import os
import csv

#Provide filepath
csv_path = os.path.join('..', 'Resources', 'election_data.csv')

#Initialise Variables. Votes_Candidate and Percentage_Votes_Candidate set as dictionaries so that we can retrieve the relevant pairs later.
Votes_count = 0
Votes_Candidate = {}
Max_Votes = 0

#Open and Access CSV file
with open(csv_path, newline="") as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csvreader)

#Iterate through each row in the dataset and increase Votes_count by 1 each time to get the total number of votes.

#Nest an 'if' function to tally the Votes per Candidate. Each new candidate resets the counter to 1.

#Set a Max_Votes variables that updates to reflect the highest value.

    for row in csvreader:
        Votes_count += 1

        if row[2] in Votes_Candidate:
            Votes_Candidate[row[2]] += 1
        else:
            Votes_Candidate[row[2]] = 1
        if Votes_Candidate[row[2]] > Max_Votes:
            Max_Votes = Votes_Candidate[row[2]]   
            election_winner = row[2] 

#Print outputs, including percentage of votes per candidate

print("Election Results")
print("-----------------------")
print(f"Total Votes: {Votes_count}")
print(f"-----------------------")
for candidate, votes in Votes_Candidate.items():
    Percentage_Votes = round((votes/Votes_count)*100, 3)
    print(f"{candidate}: {Percentage_Votes}% ({votes})")
print("-------------------------")
print(f"Winner: {election_winner}")
print(f"-------------------------")

#Write to text file

with open("Election Results.txt", "w") as text:
    text.write("Election Results\n")
    text.write("-----------------------\n")
    text.write(f"Total Votes: {Votes_count}\n")
    text.write(f"-----------------------\n")
    for candidate, votes in Votes_Candidate.items():
        Percentage_Votes = round((votes/Votes_count)*100, 3)
        text.write(f"{candidate}: {Percentage_Votes}% ({votes})\n")
    text.write("-------------------------\n")
    text.write(f"Winner: {election_winner}\n")
    text.write(f"-------------------------\n")