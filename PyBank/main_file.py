import os
import csv


budget_data = os.path.join("downloads","budget_data.csv")


Maximum_monthly_profit = 0
Minimum_monthly_profit = 0
total = 0
month_count = 0
previous_profit = 0
total_monthly_change =0




with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        num = float(row[1])
        
        total =total +num
        
        month_count = month_count +1
        
        
      
        
        monthly_profit_change = float(row[1]) - previous_profit
        
        
        previous_profit = float(row[1])
        total_monthly_change = total_monthly_change +monthly_profit_change
       
        if monthly_profit_change > Maximum_monthly_profit:
            Maximum_monthly_profit = monthly_profit_change
            greatest_month = row[0]
       
        if monthly_profit_change < Minimum_monthly_profit:
            Minimum_monthly_profit = monthly_profit_change
            lowest_month = row[0]


total = round(total)
Maximum_monthly_profit = round(Maximum_monthly_profit)
Minimum_monthly_profit = round(Minimum_monthly_profit)
avg_change = round(total_monthly_change/month_count)

pybank_data_output = (
 
f'                        Financial Analysis                             \n'
f'--------------------------------------------------------------------------\n'
f'Total Months: {month_count}\n'
f'Total: ${total}\n'
f'Average Change: ${avg_change}\n'
f'Greatest Increase in profits: {greatest_month}, (${Maximum_monthly_profit})\n'
f'Greatest Decrease in profits: {lowest_month}, (${Minimum_monthly_profit})\n'
)


print(pybank_data_output)

pybank_output = os.path.join("downloads","PyBank_Financial_Output.txt")
with open(pybank_output, 'w') as txtfile:
      txtwriter = txtfile.write(pybank_data_output)
      