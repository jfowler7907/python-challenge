import os
import csv

# identify location of variable
csvpath=os.path.join('..',"PyBank","budget_data.csv")

 # list to store the data
Months = []
total_months = 0

#Print title
print("Financial Analysis")
print("------------------------------------------")

#Open file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    for row in csvreader:
        Months.append(row[0])
        total_months+=1
print("Total Months: ", total_months)




print(csvreader)

