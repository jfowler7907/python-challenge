import os
import csv

# identify location of variable
csvpath=os.path.join("Resources","election_data2.csv")

#Create variables
count = 0
candidate_vote_count={}


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader) #skips the header
    header=next(csvreader) #skips the header

    #count the votes
    for row in csvreader: 
        #track the unique candidates and their vote counts
        if row[2] in candidate_vote_count:
            candidate_vote_count[row[2]] = candidate_vote_count[row[2]] + 1
        else:
            candidate_vote_count[row[2]] = 1

        #Track total vote count
        count = count + 1
         
      
print("Election Results")
print("-------------------------------")
print("Total Votes: " +str(count))
print("-------------------------------")
print(candidate_vote_count) 

#Create output location for text file
text_path = os.path.join("Resources", "PyPoll_Summary.txt")

with open(text_path, "w+") as text_file:
    text_file.write("Election Results {PyPoll_Summary} : \n")
    text_file.write("-------------------------------------------\n")
    text_file.write("Election Results")
    text_file.write("-------------------------------------------\n")
    text_file.write("Total Votes: " +str(count))

##Questions for TA: How to calculate the % of votes (candidate_vote_count/count) I keep getting an error

