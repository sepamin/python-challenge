import os
import csv

Data = os.path.join('C:/Users/Brendan/Documents/GitHub/python-challenge/PyBank/BudgetData.csv')
with open(Data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    totalmonths=0
    revenue=[]
    months = []
    changeList=[]
    i=0
    total_rev=0


    for row in csvreader:
        months.append(row[0])
        revenue.append(row[1])
    totalmonths=(len(months))
    revint=map(int,revenue)
    total_rev=(sum(revint))
    
    
    for i in range(len(revenue)-1):
        profitorloss=int(revenue[i+1])-int(revenue[i])
        changeList.append(profitorloss)
    tpl= sum(changeList)
    avchange=tpl/len(changeList)

    mi=max(changeList)
    md=min(changeList)

    x=changeList.index(mi)
    l=changeList.index(md)
    highestmonth=months[x+1]
    lowestmonth=months[l+1]


    
print(f"Financial Analysis")
print(f'-----------------------')

print("Total months: "  +  str(totalmonths))
print("Total $" + str(total_rev))
print("Average Change $" + str(round(avchange,2)))
print("Greatest Increase in Profits: " + highestmonth + " ($" + str(mi)+")")
print("Greatest Decrease in Profits: " + lowestmonth + " ($" + str(md)+")")

output= os.path.join('C:/Users/Brendan/Documents/GitHub/python-challenge/PyBank/FinalResults.txt')
with open(output, "w") as textfile:
    textfile.write(f"Financial Analysis")
    textfile.write(f'\n-----------------------')

    textfile.write("\nTotoal months: "  +  str(totalmonths))
    textfile.write("\nTotal $" + str(total_rev))
    textfile.write("\nAverage Change $" + str(round(avchange,2)))
    textfile.write("\nGreatest Increase in Profits: " + highestmonth + " ($" + str(mi)+")")
    textfile.write("\nGreatest Decrease in Profits: " + lowestmonth + " ($" + str(md)+")")