import os

import csv

# csv file is now linked
pybank_csv = os.path.join('..', "Resources", "budget_data.csv")

# Open csv file. Define delimiter. Define lists and starting variables
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    date = []
    pl = []
    total = 0
    sum_ch = 0
    mth_ch = 0
    mth_ct = 0
    ginc = 0
    gdec = 0
    ginc_l1 = 0
    gdec_l2 = 0
    x = 0
    y = 0
    
    # Start reading csv file and populating lists defined
    for row in csvreader:
        # Define column 1 and column 2
        mth = row[0]
        prlo = row[1]
        # Append to list date data from column 1 now defined as mth
        date.append(mth)
        # Append to list pl data from column 2 now defined as prlo
        pl.append(prlo)
        
    # Now count in date column which is defined as mth by accessing list:date and call it mth_ct
    mth_ct = len(date)
    #print(mth_ct)
    
# We now loop through list:pl using variable x as loop counter. We have to loop through all the records in list:pl as defined by mth_ct
for x in range (mth_ct):
    # for each row start with total = 0 and add to it till all records are read. Add this in list:pl which now contains data for each row
    total = total + int(pl[x])
#print(total)
    
# We now define a second loop that determines 3 things. Average of changes. Greatest increase and greatest decrease
for y in range(mth_ct-1):
    sum_ch = sum_ch + (float(pl[y+1]) - float(pl[y]))
# We now print the total and divide it by number of counts to get the average
#print(sum_ch/(mth_ct - 1))
# We now look at each individual mthly change, initialised as mth_ch. Loop through the calculated amount for each record and look for the maximum value
    mth_ch = (float(pl[y+1]) - float(pl[y]))
    if mth_ch > ginc:
        ginc = mth_ch
        ginc_l1 = y
    else:
        ginc = ginc
    if mth_ch < gdec:
        gdec = mth_ch
        gdec_l2 = y
    else:
        gdec = gdec
#print(gdec)

# Generate analysis lines. Define a string variable called results

results = f'\
Financial analysis \n\
-----------------------------\n\
Total Months: {mth_ct}\n\
Total Amount: ${total}\n\
Average Change: ${round(sum_ch/(mth_ct-1),2)}\n\
Greatest Increase in Profits: {date[ginc_l1+1]} (${int(ginc)})\n\
Greatest Decrease in Profits: {date[gdec_l2+1]} (${int(gdec)})\n'
print(results)

# Write into a text file and name it pybank.txt

# Open a file called pybank.txt and write into it
finalfile = open("pybank.txt", "w")
finalfile.writelines(results)
finalfile.close()
        



