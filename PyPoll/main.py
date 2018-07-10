import csv
from collections import defaultdict
csvpath = "/Users/Zhisen/Downloads/election_data.csv"
with open(csvpath,'r') as infile:
    election = csv.reader(infile,delimiter = ',')
    header = next(election)
    voter_count = 0
    candidates_dict = defaultdict(int)
    for row in election:
        voter_count += 1
        candidate = row[2]
        candidates_dict[candidate] += 1
    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {str(voter_count)}')
    print('----------------------------')
    candidate_names = list(candidates_dict.keys())
    for name in candidate_names:
        individual_count = candidates_dict[name]
        percent = individual_count/voter_count*100
        percent = round(percent, 3)
        print(f'{name}: {percent}% ({individual_count})')
    print('----------------------------')
    values_list = list(candidates_dict.values())
    maximum = max(values_list)
    index = values_list.index(maximum)
    winner = candidate_names[index]
    print(f'Winner: {winner}')
    print('----------------------------')

csvpath = "/Users/Zhisen/python-challenge/PyPoll/PyPoll_output.csv"
with open(csvpath,'w') as outfile:
    output = csv.writer(outfile)
    output.writerow(['Election Results'])
    output.writerow(['----------------------------'])
    output.writerow([f'Total Votes: {str(voter_count)}'])
    output.writerow(['----------------------------'])
    name1 = candidate_names[0]
    name2 =candidate_names[1]
    name3 = candidate_names[2]
    name4 = candidate_names[3]
    percent1 = round(candidates_dict[name1]/voter_count*100,3)
    percent2 = round(candidates_dict[name2]/voter_count*100,3)
    percent3 = round(candidates_dict[name3]/voter_count*100,3)
    percent4 = round(candidates_dict[name4]/voter_count*100,3)
    output.writerow([f'{name1}: {percent1}% ({candidates_dict[name1]})'])
    output.writerow([f'{name2}: {percent2}% ({candidates_dict[name2]})'])
    output.writerow([f'{name3}: {percent3}% ({candidates_dict[name3]})'])
    output.writerow([f'{name4}: {percent4}% ({candidates_dict[name4]})'])
    output.writerow(['----------------------------'])
    output.writerow([f'Winner: {winner}'])
    output.writerow(['----------------------------'])




    

