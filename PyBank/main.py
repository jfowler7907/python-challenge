import os
import csv

# identify location of variable
csvpath=os.path.join("Resources","budget_data.csv")

 # list to store the data
profit = []
monthly_changes = []
date = []

# define variables
 
count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0

# Open the CSV using the set path PyBank.csv

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)

    # Conducting the ask
    for row in csvreader:    
    # Use count to count the number months in this dataset
        count = count+1
        date.append(row[0])
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit
        monthly_changes.append(monthly_change_profits)
        total_change_profits = total_change_profits + monthly_change_profits
        initial_profit = final_profit
        average_change_profits = (total_change_profits/count)

    #greatest min and max
    greatest_increase_profits = max(monthly_changes)
    greatest_decrease_profits = min(monthly_changes)

    increase_date = date[monthly_changes.index(greatest_increase_profits)]
    decrease_date = date[monthly_changes.index(greatest_decrease_profits)]

#Prtint Summary Page
print(count)
print("------------------------------------------------------")
print("Financial Analysis")
print("------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " "$" + str(total_profit))
print("Average change: " +"$" + str(average_change_profits))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")")
print("------------------------------------------------------")

#Create output location for text file
text_path = os.path.join("Resources", "PyBank_Summary.txt")

with open(text_path, "w+") as text_file:
    
#Create text file
    text_file.write("Financial Analysis {PyBank_Summary} : \n")
    text_file.write("-------------------------------------------\n")
    text_file.write("Financial Analysis")
    text_file.write("-------------------------------------------\n")
    text_file.write("Total Months: " + str(count) + "\n")
    text_file.write("Total Profits: " +"$" + str(total_profit) + "\n")
    text_file.write("Average change: " + "$" + str(average_change_profits) + "\n")
    text_file.write("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text_file.write("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text_file.write("-------------------------------------------\n")
    text_file.write.close()







