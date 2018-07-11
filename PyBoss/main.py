import csv
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

csvpath1="/Users/Zhisen/Downloads/employee_data.csv"
csvpath2="/Users/Zhisen/python-challenge/PyBoss/converted_employee_data.csv"
with open(csvpath1,'r') as infile, \
     open(csvpath2,'w') as outfile:
     data = csv.reader(infile,delimiter = ',')
     output = csv.writer(outfile)
     header = next(data)
     output.writerow(["Emp ID","First Name","Last Name","DOB","SSN","State"])
     for row in data:
         empid,name,dob,ssn,state = row
         first_name,last_name = row[1].split(' ')
         y,m,d = row[2].split('-')
         _, _, ssn = row[3].split('-')
         new_dob = f'{m}/{d}/{y}'
         new_ssn = f'***-**-{ssn}'
         state_abb = us_state_abbrev[state]
         output.writerow([empid,first_name,last_name,new_dob,new_ssn,state_abb])
    
