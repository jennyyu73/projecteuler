#pandigitalPrime
import time
start=time.time()
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter

def isPandigitalModified(n):
    temp=abs(n)
    for i in range (1,digitCount(n)+1,1):
        counter=0
        for h in range(1,digitCount(n)+1,1):
            digit=n%10
            n=n//10
            if i==digit:
                counter=counter+1
        if counter==0:
            return False
        n=temp
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
print(isPandigitalModified(1234))
listofprimes=sieveOfEratosthenes(9876543)
panprimes=[]
for i in range(len(listofprimes)):
    truefalse=isPandigitalModified(listofprimes[i])
    if truefalse==True:
        panprimes.append(listofprimes[i])
end=time.time()
print(max(panprimes))
print(end-start,"seconds")

