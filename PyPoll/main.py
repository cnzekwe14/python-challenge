import os
import csv

csv_path_1 = os.path.join('.','Resources', 'election_data.csv')

with open ("text_3.txt", "w") as output_1:
    with open(csv_path_1, encoding='utf') as election_csv:
        csvreader = csv.reader(election_csv, delimiter=',')
        print(csvreader)
        
        header = next(csvreader) # start data analysis in the next row
        election_1 = [] # get all data into a list
        candidates_1 = [] # get the candidates into a list
        c = []
        # print("Election Results")
        a = print("Election Results")
        # print("-----------------------")
        for row in csvreader:
            election_1.append(row) # put all information into the list
            candidates_1.append(row[2]) # put all candidates names into a list.  This is not distinct
        
        # print(f'Total Votes: {len(election_1)}') # print the total votes
        # print("-----------------------")
        people = [x for x in set(candidates_1)] # get me the list of candidates.  This is distinct
        # print(people)
        counts = [candidates_1.count(vote) for vote in set(candidates_1)] # count how many time they were selected 
        # print(counts)
        dict_list = dict(zip(people,counts)) # put this in a dictionary to get the candidate with there total count
        sum_counts = sum(counts) # get the total count of votes
        for i in dict_list: # for key in the list 
            x = ((dict_list[i])/sum_counts)*100 # the key values divided by the sum of all votes
            print(f'{i}:{round(x,3)}% ({dict_list[i]})') # get the candidate percentage and vote
        print("---------------------")
        winner = max(dict_list, key=dict_list.get) # get the maximum value in the dictionary and returns the key
        # print(f'Winner: {winner}') # print the winner name
        # print("---------------------")

        out_1 = "Election Results"
        out_2 = "------------------"
        # print("-----------------------"),
        # print(f'Total Votes: {len(election_1)}'),
        # print("-----------------------"),
        # print(f'Winner: {winner}'), 
        # print("---------------------"))
    output_1.write(out_1)
    output_1.write(out_1)
    output_1.close()
