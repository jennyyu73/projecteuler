def isPalindrome(n):
	reverseN=str(n)[::-1]
	return str(n) == reverseN and reverseN[0] != "0"

def turnToBinary(n):
	result=""
	while n != 0:
		result= str(n%2) + result
		n=n//2
	return result

palSum=0

for n in range(1000000):
	if isPalindrome(n) and isPalindrome(turnToBinary(n)):
		palSum += n

print(palSum)