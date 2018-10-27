#62 cubic permutations
import itertools

def kthDigit(n,k):
    return (abs(n)//10**k)%10
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
while 1==1:
    permcount=1
    cubec=405
    cubenum=cubec**3
    digits=[]
    for i in range(digitCount(cubenum)):
        digits.append(kthDigit(cubenum,i))
    permutations=itertools.permutations(digits)
    for i in range(len(permutations)):
        permcandidate=permutations[i]
        permnum=0
        for k in range(len(permcandidate)):
            permnum=permnum+permcandidate[k]
            permnum=permnum*10
        if permnum**(1/3)==int(permnum**(1/3)):
            permcount+=1
    if permcount==5:
        break
    cubec+=1
print(cubec**3)
