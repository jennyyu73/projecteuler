#45 triangular pentagonal and hexagonal
import math

"""
def isHexagonal(hexnum):
    hexindex=1/4+(math.sqrt(1-4*2*-hexnum))/4
    if hexindex==int(hexindex):
        return True
    else:
        return False
print(isHexagonal(1533776805))

def isPentagonal(pentnum):
    pentindex=1/6+math.sqrt(1-4*3*(-2*pentnum))/6
    if pentindex==int(pentindex):
        return True
    else:
        return False

print(isPentagonal(1533776805))

while 1==1:
    hexindex=166
    hexnum=hexindex*(2*hexindex-1)
    if isPentagonal(hexnum)==True:
        break
    hexindex+=1
print(hexnum)
"""
def isHexagonal(hexnum):
    hexindex=1/4+(math.sqrt(1-4*2*-hexnum))/4
    if hexindex==int(hexindex):
        print(hexindex)
        return True
    else:
        return False
print(isHexagonal(1533776805))
    
import time
start=time.time()

hexagonal=[]
pentagonal=[]
penthex=0
for i in range(27000,32000):
    hexagonal.append(i*(2*i-1))
    pentagonal.append(i*(3*i-1)/2)
for i in range(len(pentagonal)):
    if hexagonal.count(pentagonal[i])==1:
        penthex=pentagonal[i]
        print(i)
        break

print(penthex)
end=time.time()
print(end-start,"seconds")


