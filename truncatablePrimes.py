def isPrime(n):
	if n < 2:
		return False
	elif n == 2:
		return True
	elif n % 2 == 0:
		return False
	maxFactor=round(n**0.5)
	for i in range(3, maxFactor+1, 2):
		if n % i == 0:
			return False
	return True

def isRightTruncatablePrime(n):
	while n > 0:
		if not isPrime(n):
			print(n)
			return False
		n=n//10
	return True

def isLeftTruncatablePrime(n):
	strN=str(n)
	while strN != "":
		if not isPrime(int(strN)):
			return False
		strN=strN[1:]
	return True

count=0
guess=10
primeSum=0

while count != 11:
	guess += 1
	if isRightTruncatablePrime(guess) and isLeftTruncatablePrime(guess):
		count += 1
		primeSum += guess
		print(count)

print(primeSum)