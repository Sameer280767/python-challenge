import os

import csv

# csv file is now linked
pypoll_csv = os.path.join('..', "Resources", "election_data.csv")

# Open csv file. Define delimiter. Read the header row first. Define lists and starting variables
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    # We are now going to generate 7 lists. First 3 lists are for columns in the csv file. Next 4 are lists which will contain data required in the question
    # 3 lists for columns
    voterid = []
    country = []
    candidate = []
    # 4 lists for storing result
    cannames = []
    canrcvvotes = []
    percanvotesrec = []
    canresult= []
    # Variables initialised as zero. And 4 loop counters a, b, c, d
    votesw = 0
    votesl = 0
    lcount = 0
    a = 0
    b = 0
    c = 0
    d = 0
    
    for row in csvreader:
        # Define column headings for each row voter id: void, country: coid, candidate: caid
        void = row[0]
        coid = row[1]
        caid = row[2]
        #Append data to 3 lists namely voterid, country, candidate
        voterid.append(void)
        country.append(coid)
        candidate.append(caid)
        
    # Total number of votes is now the count of records in list voterid
    lcount = len(voterid)
    #print(lcount)python main_1.py


# We now load the first candidates name to comapare
cannames.append(caid)
# We now create a loop to get number of candidates who received a vote
for a in range(lcount-1):
    if candidate[a + 1] != candidate[a] and candidate[a+1] not in cannames:
        cannames.append(candidate[a+1])
        
i = len(cannames)
#print(i)

# Using the number of candidates we now name each candidate and votes they received
for b in range(i):
    canrcvvotes.append(candidate.count(cannames[b]))
    
#print(cannames)
#print(canrcvvotes)

# We will now calculate votes received by winner and loser. To do so we will preload loser votes variable:votesl with maximum number of votes which is in lcount
votesl = lcount

for c in range(i):
    percanvotesrec.append(f'{round(canrcvvotes[c]/lcount * 100, 4)}%')
    if canrcvvotes[c] > votesw:
        winner = cannames[c]
        votesw = canrcvvotes[c]
    if canrcvvotes[c] < votesl:
        loser = cannames[c]
        votesl = canrcvvotes[c]
for d in range(i):
    canresult.append(f'{cannames[d]}: {percanvotesrec[d]} ({canrcvvotes[d]})')
    

# Set up to print final result for each candidate
finalresult = 'n'.join(canresult)   

# Final presentation
final_report = f'\
Election Results\n\
----------------------------\n\
Total Votes: {lcount}\n\
----------------------------\n\
{finalresult} \n\
-----------------------------------------------------------------------------------------------------------------\n\
Winner: {winner} \n\
----------------------------\n'

print(final_report)

#Write into text file named pypoll.txt. If file does not exist a nww file will be created
# Final report will be written into the file pypoll.txt
#File will then be closed

file1=open("pypoll.txt","w") 
file1.writelines(final_report) 
file1.close() 

    





        

    
        
    

    
    
