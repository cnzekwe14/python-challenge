import os
import csv



csvfile = os.path.join('.','Resources', 'budget_data.csv') # get the path of the data
with open("PyBank.txt","w") as PyBank_output: # create a text file with the information provided below
    with open(csvfile,encoding ='utf') as budget_csv: # open the csv file an assign it a variable
        csvreader = csv.reader(budget_csv, delimiter=",") # read in the budget_data and seperate it by commas
        print(csvreader) # provide the reader information

        header = next(csvreader) # starts data on the next row
        total_month_count = 0 # store the count of all rows which provides month count
        budget_1 = [] # store budget values in this list
        total_budget = 0 # used to get the total sum of budget
        month_1 = [] # store month in this list

        for row in csvreader:
            total_month_count+=1
            budget_1.append(row[1])
            month_1.append(row[0])


        for x in budget_1:
            total_budget+=  float(x) # sums all data and gets the total
            
        budget_t = round(total_budget,) # store the total budget to output into text file
        profit_change = round((float(budget_1[len(budget_1) -1]) - float(budget_1[0]))/float(len(budget_1)-1),2) # used to get the average change
            

        first_number = 0 # looks the first number
        second_number = 0 # looks at second number
        profits_review = [] # used to append data to review max and min
        for i in budget_1:
            second_number = second_number + 1 # get the next second number
            if(second_number < len(budget_1)): # second number is less than the total number
                first_1 = budget_1[first_number] # assign first number 
                second_1 = budget_1[second_number] # assign second number
                profits_sub= float(second_1)-float(first_1) # second num - first num to get the gains and losses
                profits_review.append(profits_sub) # put the gains and losses in a list
                first_number = first_number + 1 # got to the next first number
            else:
                0

        max_number = round(max(profits_review),) # get the max number in the list of gains and losses   
        min_number = round(min(profits_review),) # get the min number in the list of gains and losses
        month_min = profits_review.index(min_number) +1 # find the index of the biggest loss within the list of gains and losses
        month_max = profits_review.index(max_number) +1 # find the index of the highest gains within the list of gains and losses
        m1 = month_1[month_max] # get the month that had the highest gains
        m2 = month_1[month_min] #get the month that had the biggest loss
    
        # provide the output into the terminal
        print('Financial Analysis')
        print('------------------------------')
        print(f'Total Months: {total_month_count}')   
        print(f'Total: ${round((total_budget),)}')
        print(f'Average Change: ${profit_change}')
        print(f'Increase in Profits: {m1} (${max_number})')
        print(f'Decrease in Profits: {m2} (${min_number})')

        # provide the output into the text file
        out_1 = f'Financial Analysis\n--------------------------------\nTotal Months: {total_month_count}'
        out_2 = f'\nTotal: ${budget_t}\nAverage Change: ${profit_change}'
        out_3 = f'\nIncrease in Profts: "{m1} (${max_number})\nDecrease in Profits: {m2} (${min_number})'
        PyBank_output.write(out_1) 
        PyBank_output.write(out_2)
        PyBank_output.write(out_3)
    PyBank_output.close()

