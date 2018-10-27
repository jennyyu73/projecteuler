#longestCollatzSequence

def collatz(num):
    if num/2==int(num/2):
        return num/2
    else:
        return 3*num+1

maxcollatzcounter=0
startnum=0
for i in range(2,1000000):
    collatzcounter=0
    num=i
    while num!=1:
        num=collatz(num)
        collatzcounter+=1
    if collatzcounter>maxcollatzcounter:
        maxcollatzcounter=collatzcounter
        startnum=i

print(startnum)
