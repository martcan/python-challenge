# Pybank
import os
import csv

csvpath=os.path.join('Resources','budget_data.csv')

#Initial variables, the monly_profit_change and month would be arrays 
total_months=0
total=0
previous_month_profit=0
monthly_profit_change=[]
month=[]


with open(csvpath) as csvfile:

    csvreader=csv.reader(csvfile,delimiter=',')
    
    #Skipping the header on the fist row of the csv
    csv_header=next(csvreader)


#Read each row of data after header
    for row in csvreader:
        month.append(row[0])
        total_months=total_months+1
        total=int(total+float(row[1]))
        current_month_profit_change=float(row[1])-previous_month_profit
        #Conditional to calculate the monthly_profit_change
        if previous_month_profit !=0:
            monthly_profit_change.append(current_month_profit_change)
        #the previous_month_profit is now assigned to a new value
        previous_month_profit=float(row[1])

#Calculate average_change(using round function to limit 2 digits after decimal point),the greatest increase and decrease in Profits
average_profit_change=round((sum(monthly_profit_change)/len(monthly_profit_change)),2)
        
greatest_profit_increase=int(max(monthly_profit_change))

greatest_profit_decrease=int(min(monthly_profit_change))

#Find the index of greatest_profit_increase and the greatest_profit_decrease inside the array
max_index=monthly_profit_change.index(greatest_profit_increase)
min_index=monthly_profit_change.index(greatest_profit_decrease)

#Print the report
print(f"Financial Analysis") 
print(f"----------------------------")
print(f"Tota Months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_profit_change}")
#beware that the index in the month array leads by 1 compared to the monthly_profit_change array
print(f"Greatest Increase in Profits: {month[max_index+1]} (${greatest_profit_increase})")
print(f"Greatest Decrease in Profits: {month[min_index+1]} (${greatest_profit_decrease})")

#Write the report to txt file with a designated path
designatedpath=os.path.join('analysis','financial_analysis.txt')
with open(designatedpath, 'w') as text:
    text.write(f"Financial Analysis"+"\n")
    text.write(f"----------------------------"+"\n")
    text.write(f"Tota Months: {total_months}"+"\n")
    text.write(f"Total: ${total}""\n")
    text.write(f"Average Change: ${average_profit_change}""\n")
    text.write(f"Greatest Increase in Profits: {month[max_index+1]} (${greatest_profit_increase})""\n")
    text.write(f"Greatest Decrease in Profits: {month[min_index+1]} (${greatest_profit_decrease})""\n")