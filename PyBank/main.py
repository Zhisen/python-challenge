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
    maximum = max(change_list)
    max_index = change_list.index(maximum) + 1
    max_month = month_list[max_index]
    minimum = min(change_list)
    min_index = change_list.index(minimum) + 1
    min_month = month_list[min_index]
    
    print('Financial Analysis')
    print('-------------------------')
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_net}")
    print(f"Average Change : {average: .2f}")
    print(f"Greatest Increase in Profits: {max_month} (${maximum})")
    print(f"Greatest Decrease in Profits: {min_month} (${minimum})")
    title = 'Financial Analysis'
    line = '-------------------------'
    text1 = f"Total Months: {month_count}"
    text2 = f"Total: ${total_net}"
    text3 = f"Average Change : {average: .2f}"
    text4 = f"Greatest Increase in Profits: {max_month} (${maximum})"
    text5 = f"Greatest Decrease in Profits: {min_month} (${minimum})"
path = '/Users/Zhisen/python-challenge/PyBank/PyBank_output.txt'
with open(path, 'w') as outfile:
    output = outfile
    output.writelines(f'{title}\n{line}\n{text1}\n{text2}\n{text3}\n{text4}\n{text5}')

