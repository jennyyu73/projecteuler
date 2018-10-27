#Euler 12: Highly divisible triangular number

import math

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

def smallestPrimeFactor(n):
    a=sieveOfEratosthenes(math.ceil(math.sqrt(n)))
    for i in range(len(a)):
        if n%a[i]==0:
            return a[i]

def factorization(n):
    allfactors=[]
    while isPrime(n)==False:
        smallestpfactor=smallestPrimeFactor(n)
        n=n/smallestpfactor
        allfactors.append(n)
        if allfactors.count(smallestpfactor)==0:
            allfactors.append(smallestpfactor)
    if allfactors.count(n)==0:
        allfactors.append(n)
    return sorted(allfactors)

add=8
triangle=28
#while len(factorization(triangle))<=500:
 #   triangle+=add
  #  add+=1
print(factorization(12))





