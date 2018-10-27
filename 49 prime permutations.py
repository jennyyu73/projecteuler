#49 prime permutations

def sieveOfEratosthenes(n):
    a=[]
    sieve=[True for i in range(n+1)]
    for i in range(2,n+1):
        if sieve[i]==True:
            a.append(i)
            for j in range (i**2,n+1,i):
                sieve[j]=False
    return a
def isPrime(n):
    if n<=1:
        return False
    if n==2:
        return True
    elif int(n/2)==n/2:
        return False
    for i in range (3,int(math.sqrt(n))+1,2):
        if n%i==0:
            return False
    return True
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
def kthDigit(n,k):
    return (abs(n)//10**k)%10
import itertools
def threePrimes(n):
    digits=[]
    for i in range(digitCount(n)):
        digits.append(kthDigit(n,i))
    digitpermutations=list(itertools.permutations(digits))
    primecount=0
    fourdigitprime=0
    for i in range(len(digitpermutations)):
        for k in range(0,4):
            fourdigitprime+=digitpermutations[i][k]
            fourdigitprime
    if primecount=4:
        return True
    else:
        return False
    
fourdigitprimes=sieveOfEratosthenes(9999)
fourdigitstart=0
for i in range(len(fourdigitprimes)):
    if digitCount(fourdigitprimes[i])==4:
        fourdigitstart=i
        break
fourdigitprimes=fourdigitprimes[168:]
for i in range(len(fourdigitprimes)):
    if threePrimes(fourdigitprimes[i]):
        print(fourdigitprimes[i])
        break
    
