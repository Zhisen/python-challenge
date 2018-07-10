import csv
from statistics import mean
csvpath = '/Users/Zhisen/Downloads/budget_data.csv'
with open(csvpath, 'r') as csvfile:
    budget = csv.reader(csvfile, delimiter=',')
    header = next(budget)
    month_count = 0 
    total_net = 0
    profit_list = []
    month_list = []
    for row in budget:
        month_count += 1
        total_net = total_net + int(row[1])
        profit = row[1]
        month = row[0]
        profit_list.append(profit)
        month_list.append(month)
    i = 1
    change_list = []
    while i < month_count:
        change = int(profit_list[i]) - int(profit_list[i-1])
        change_list.append(change)
        i = i + 1
    average = mean(change_list)
    average = round(average, 2)
    maximum = max(change_list)
    max_index = change_list.index(maximum) + 1
    max_month = month_list[max_index]
    minimum = min(change_list)
    min_index = change_list.index(minimum) + 1
    min_month = month_list[min_index]
    
    print("Total Months: " + str(month_count))
    print("Total: $" + str(total_net))
    print("Average Change : " + str(average))
    print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(maximum) + ")")
    print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(minimum) + ")")
    text1 = "Total Months: " + str(month_count)
    text2 = "Total: $" + str(total_net)
    text3 = "Average Change : " + str(average)
    text4 = "Greatest Increase in Profits: " + str(max_month) + " ($" + str(maximum) + ")"
    text5 = "Greatest Decrease in Profits: " + str(min_month) + " ($" + str(minimum) + ")"
csvpath = '/Users/Zhisen/Downloads/PyBank_output.csv'
with open(csvpath, 'w') as outfile:
    output = csv.writer(outfile)
    output.writerows([[text1],[text2],[text3],[text4],[text5]])
