def sieveOfEratosthenes(n):
    a=[]
    sieve=[True for i in range(n+1)]
    for i in range(2,n+1):
        if sieve[i]==True:
            a.append(i)
            for j in range (i**2,n+1,i):
                sieve[j]=False
    return a

primes=sieveOfEratosthenes(9999)
primes=set(primes)

for n in primes:
	num=n
	if len(str(n)) > 3:
		for i in range(2):
			num+=3330
			if (num not in primes) or not(''.join(sorted(list(str(n)))) == ''.join(sorted(list(str(num))))):
				break
			if i == 1:
				print(n)
				break

