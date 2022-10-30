import os
import csv

csv_path_1 = os.path.join('.','Resources', 'election_data.csv') # get the csv file
csv_path_2 = os.path.join('.','analysis','PyPoll.txt') # get the text file
with open (csv_path_2, "w") as output_2: # create a texxt file for the output below
    with open(csv_path_1, encoding='utf') as election_csv:
        csvreader = csv.reader(election_csv, delimiter=',')
        print(csvreader)
        
        header = next(csvreader) # start data analysis in the next row
        election_1 = [] # get all data into a list
        candidates_1 = [] # get the candidates into a list
        print("Election Results")
        print("-----------------------")
        for row in csvreader:
            election_1.append(row) # put all information into the list
            candidates_1.append(row[2]) # put all candidates names into a list.  This is not distinct
        
        print(f'Total Votes: {len(election_1)}') # print the total votes
        a = len(election_1)
        print("-----------------------")
        people = [x for x in set(candidates_1)] # get me the list of candidates.  This is distinct
        # print(people)
        counts = [candidates_1.count(vote) for vote in set(candidates_1)] # count how many time they were selected 
        # print(counts)
        dict_list = dict(zip(people,counts)) # put this in a dictionary to get the candidate with there total count
        sum_counts = sum(counts) # get the total count of votes
        candidate_part = []
        for i in dict_list: # for key in the list 
            x = ((dict_list[i])/sum_counts)*100 # the key values divided by the sum of all votes
            print(f'{i}:{round(x,3)}% ({dict_list[i]})') # get the candidate percentage and vote
            candidate_add = f'{i}:{round(x,3)}% ({dict_list[i]})'
            candidate_part.append(candidate_add)
        print("---------------------")
        winner = max(dict_list, key=dict_list.get) # get the maximum value in the dictionary and returns the key
        print(f'Winner: {winner}') # print the winner name
        print("-----------------------")
       
    # out the results above in a textfile
    out_1 = f'Election Results\n-----------------\nTotal Votes: {a}\n----------------------\n'
    output_2.write(out_1)
    for new_1 in candidate_part:
        p = new_1 +"\n"
        output_2.write(p)
    out_2 = f'-----------------------\nWinner: {winner}\n----------------------'
    output_2.write(out_2)
    output_2.close()
