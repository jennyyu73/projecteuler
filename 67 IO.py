import csv

with open('triangle.txt', newline='') as inputfile:
    results = list(csv.reader(inputfile))
triangle=[]
for i in range(len(results)):
    string=results[i]
    print(string)
    triangle.append(string.split())
print(triangle[12])
