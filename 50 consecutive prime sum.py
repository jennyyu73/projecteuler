#project euler 50 consecutive prime sum

def sieveOfEratosthenes(n):
    a=[]
    sieve=[True for i in range(n+1)]
    for i in range(2,n+1):
        if sieve[i]==True:
            a.append(i)
            for j in range (i**2,n+1,i):
                sieve[j]=False
    return a

primes=sieveOfEratosthenes(999999)
for i in range(len(primes)-1,-1,-1):
    candidate=primes[i]
    for k in range(i):
        primesum=0
        for j in range(k,i):
            while primesum<candidate:
                primesum+=1
