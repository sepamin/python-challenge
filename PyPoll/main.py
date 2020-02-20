import os
import csv
import statistics
from statistics import mode

Poll = os.path.join('C:/Users/Brendan/Documents/GitHub/python-challenge/PyPoll/ElectionData.csv')
with open(Poll, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    percent0=0
    percent1=0
    percent2=0
    percent3=0
    cCount=[]
    votes=[]
    uniques=[]
    candidates=[]
    counts=0
    for row in csvreader:
        counts=counts+1
        if row[2] not in uniques:
            uniques.append(row[2])
        votes.append(row[2])
    for candidates in uniques:
        cCount.append(votes.count(candidates))
    
    
    percent0=((cCount[0])/counts)*100
    percent1=((cCount[1])/counts)*100
    percent2=((cCount[2])/counts)*100
    percent3=((cCount[3])/counts)*100

    winnner=mode(votes)

print(f"Election Results")
print(f"---------------------")
print("Total Votes: " + str(counts))
print(f"---------------------")
print(uniques[0] + ": %" + str(round(percent0,5))+ " (" + str(cCount[0])+")")
print(uniques[1] + ": %" + str(round(percent1,5))+ " (" + str(cCount[1])+")")
print(uniques[2] + ": %" + str(round(percent2,5))+ " (" + str(cCount[2])+")")
print(uniques[3] + ": %" + str(round(percent3,5))+ " (" + str(cCount[3])+")")
print(f"---------------------")
print("Winner: " + winnner)


output= os.path.join('C:/Users/Brendan/Documents/GitHub/python-challenge/PyPoll/FinalResults.txt')
with open(output, "w") as textfile:
    textfile.write(f"Election Results")
    textfile.write(f"\n---------------------")
    textfile.write("\nTotal Votes: " + str(counts))
    textfile.write(f"\n---------------------")
    textfile.write("\n")
    textfile.write(uniques[0] + ": %" + str(round(percent0,5))+ " (" + str(cCount[0])+")")
    textfile.write("\n")
    textfile.write(uniques[1] + ": %" + str(round(percent1,5))+ " (" + str(cCount[1])+")")
    textfile.write("\n")
    textfile.write(uniques[2] + ": %" + str(round(percent2,5))+ " (" + str(cCount[2])+")")
    textfile.write("\n")
    textfile.write(uniques[3] + ": %" + str(round(percent3,5))+ " (" + str(cCount[3])+")")
    textfile.write(f"\n---------------------")
    textfile.write("\nWinner: " + winnner)