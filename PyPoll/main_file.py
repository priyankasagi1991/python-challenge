import os
import csv


Pypoll_csv = os.path.join("downloads","PyPoll_data.csv")


total_votes = 0
individual_candidate = []
candidate_vote_count = []


with open(Pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
       
        total_votes =total_votes+ 1
       
        candidate = (row[2])
        
        if candidate in individual_candidate:
            candidate_index = individual_candidate.index(candidate)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            
            individual_candidate.append(candidate)
            candidate_vote_count.append(1)




max_votes = candidate_vote_count[0]
percent = []
max_index = 0

for x in range(len(individual_candidate)):
    
    vote_percent = round(candidate_vote_count[x]/total_votes*100, 2)
    percent.append(vote_percent)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = individual_candidate[max_index] 



print('--------------------------------------------')
print('                  Election Results          ')
print('-------------------------------------------')
print(f'Total Votes: {total_votes}')
print('--------------------------------------------')
for x in range(len(individual_candidate)):
    print(f'{individual_candidate[x]} : {percent[x]}% ({candidate_vote_count[x]})')
print('---------------------------------------------')
print(f'Election winner: {election_winner.upper()}')
print('--------------------------------------------')

output_file = os.path.join("downloads","pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('----------------------------------\n')
    datafile.write('                 Election Results \n')
    datafile.write('-----------------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('-----------------------------------\n')
    for x in range(len(individual_candidate)):
        datafile.write(f'{individual_candidate[x]} : {percent[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('-----------------------------------\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('-------------------------------------\n')
     
      
