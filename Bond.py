import csv

'''DrawList = input('Enter Draw list name.')'''

dList = []
with open('100.csv', "r") as fDraw:
    reader = csv.reader(fDraw, delimiter='\t')
    for line in reader:
        for i in line:
            dList.append(i)

dList.sort()

print(dList)
with open('Out.csv', 'w') as f:
    for i in dList:
        f.writelines(i)
        f.writelines('\n')
