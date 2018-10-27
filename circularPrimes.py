#sieveOfEratosthenes
def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n%2 == 0:
		return False
	maxFactor=round(n**0.5)
	for i in range(3, maxFactor+1, 2):
		if n%i == 0:
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

primes=sieveOfEratosthenes(999999)
circularCount=0

def rotate(n):
	n=str(n)
	return int(n[len(n)-1]+n[:-1])

def isCircularPrime(n):
	for i in range(len(str(n))):
		if not isPrime(n):
			return False
		n=rotate(n)
	return True

for n in primes:
	if isCircularPrime(n):
		print(n)
		circularCount +=1

print(circularCount)

