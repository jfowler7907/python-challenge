import os
import csv

# identify location of variable
csvpath=os.path.join("Resources","election_data2.csv")

#Create variables
count = 0


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    #count the votes
    for row in csvreader:
        count= count +1

#count the candidates
total_votes = len(candidate)

#Count Khan
if candidate = "Khan":
    sum(voter_id) for x in 


 

        
print("Election Results")
print("-------------------------------")
print("Total Votes: " +str(count))
print("-------------------------------")
print(Khan_total)

##Questions for TA: How to sum candidates votes?
## Example: IF Candidate = Khan, SUM votes

