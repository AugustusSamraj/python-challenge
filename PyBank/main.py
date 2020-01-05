import os

# Module for reading CSV files
import csv
from statistics import mean
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
outputpath = os.path.join('.', 'Output', 'Financial_Analysis_Summary.txt')
monthList =[]
profitList =[]
profitChange= []
with open(csvpath, newline='', encoding="utf-8") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        #monthcount = monthcount +1
        #total = total + int(row[1])
        monthList.append(row[0])
        profitList.append(int(row[1]))
   
    for i in range(len(profitList)-1) :        
        profitChange.append(profitList[i+1]-profitList[i])
                          
maxvalueIncrease = max(profitChange)
maxvalueDecrease = min(profitChange)
maxvalueIncreaseMonth = monthList[profitChange.index(max(profitChange)) + 1]
maxvalueDecreaseMonth = monthList[profitChange.index(min(profitChange)) + 1]

# Finding Average Change by Summing all the ProfitChange List and divided
AverageChange =round(sum(profitChange)/len(profitChange),2)

# Using Mean from Statistics Library
ChangeAverage=mean(profitChange)
#print(ChangeAverage)

                     
# Print Statements

print("Python Challenge Financial Analysis")
print("------------------------------------")
print(f"Total No of Months: {len(monthList)}")
print(f"Net Total of Profit/Loss: ${sum(profitList)}")
print(f"Average Change: {AverageChange}")
print(f"Greatest Increase (in Profits): {maxvalueIncreaseMonth} ${(str(maxvalueIncrease))}")
print(f"Greatest Decrease (in Profits): {maxvalueDecreaseMonth} ${(str(maxvalueDecrease))}")
          
with open(outputpath,"w") as file:
   
    file.write("Financial Analysis\n")
    file.write("-----------------------------------\n")
    file.write(f"Total No of Months: {len(monthList)} \n")
    file.write(f"Net Total of Profit/Loss: ${sum(profitList)}\n")
    file.write(f"Average Change: {AverageChange}\n")
    file.write(f"Greatest Increase (in Profits): {maxvalueIncreaseMonth} ${(str(maxvalueIncrease))}\n")
    file.write(f"Greatest Decrease (in Profits): {maxvalueDecreaseMonth} ${(str(maxvalueDecrease))}")
