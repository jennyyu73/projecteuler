#Euler 29: distinct powers
import copy

terms=[]
for i in range(2,101):
    for k in range(2,101):
        terms.append(i**k)

distinctterms=copy.deepcopy(terms)
for i in range(len(terms)):
    count=terms.count(terms[i])
    if distinctterms.count(terms[i])!=1:
        for k in range(count-1):
            distinctterms.remove(terms[i])
print(len(distinctterms))
        

