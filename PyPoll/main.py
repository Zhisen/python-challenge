import csv
from collections import defaultdict
csvpath1 = "/Users/Zhisen/Downloads/election_data.csv"
path2 = "/Users/Zhisen/python-challenge/PyPoll/PyPoll_output.txt"
with open(csvpath1,'r') as infile, \
     open(path2,'w') as outfile:
    election = csv.reader(infile,delimiter = ',')
    output = outfile
    header = next(election)
    voter_count = 0
    candidates_dict = defaultdict(int)
    for row in election:
        voter_count += 1
        candidate = row[2]
        candidates_dict[candidate] += 1
    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {(voter_count)}')
    print('----------------------------')
    output.write('Election Results\n')
    output.write('----------------------------\n')
    output.write(f'Total Votes: {(voter_count)}\n')
    output.write('----------------------------\n')
    candidate_names = list(candidates_dict.keys())
    for name in candidate_names:
        individual_count = candidates_dict[name]
        percent = individual_count/voter_count*100
        text= f'{name}: {percent: .3f}% ({individual_count})'
        print(text)
        output.write(f'{text}\n')
    print('----------------------------')
    output.write('----------------------------\n')
    values_list = list(candidates_dict.values())
    maximum = max(values_list)
    index = values_list.index(maximum)
    winner = candidate_names[index]
    print(f'Winner: {winner}')
    print('----------------------------')
    output.write(f'Winner: {winner}\n')
    output.write('----------------------------\n')




    

