#47 distinct primes factors
import math
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
def sieveOfEratosthenes(n):
    a=[]
    sieve=[True for i in range(n+1)]
    for i in range(2,n+1):
        if sieve[i]==True:
            a.append(i)
            for j in range (i**2,n+1,i):
                sieve[j]=False
    return a
def distinctPrimeFactorization(n):
    primefactors=[]
    a=sieveOfEratosthenes(math.ceil(math.sqrt(n)))
    index=0
    while isPrime(n)==False:
        if n%a[index]==0:
            primefactors.append(a[index])
            n=n/a[index]
        else:
            index+=1
    primefactors.append(int(n))
    distinctprimefactors=[]
    for i in range(len(primefactors)):
        if distinctprimefactors.count(primefactors[i])==0:
            distinctprimefactors.append(primefactors[i])
    return distinctprimefactors
import time
start=time.time()
count=0
euler47=0
for i in range(50000,500000):
    a=distinctPrimeFactorization(i)
    if len(a)==4:
        count+=1
    else:
        count=0
    if count==4:
        euler47=i-3
        break
print(euler47)
end=time.time()
print(end-start,"seconds")

    
