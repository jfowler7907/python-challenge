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


        
print("Election Results")
print("-------------------------------")
print("Total Votes: " +str(count))
print("-------------------------------")


#Create output location for text file
text_path = os.path.join("Resources", "PyPoll_Summary.txt")

with open(text_path, "w+") as text_file:
    text_file.write("Election Results {PyPoll_Summary} : \n")
    text_file.write("-------------------------------------------\n")
    text_file.write("Election Results")
    text_file.write("-------------------------------------------\n")
    text_file.write("Total Votes: " +str(count))

##Questions for TA: How to sum candidates votes?
## Example: IF Candidate = Khan, SUM votes

