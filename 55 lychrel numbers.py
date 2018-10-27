#lychrel numbers
def kthDigit(n,k):
    return (abs(n)//10**k)%10
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
def isPalindrome(n):
    dc=digitCount(n)
    if dc/2==int(dc/2):
        for i in range(0,int(dc/2),1):
            rightdigit=kthDigit(n,i)
            leftdigit=kthDigit(n,dc-i-1)
            if rightdigit!=leftdigit:
                return False
        return True
    else:
        dc=dc-1
        for i in range(0,int(dc/2),1):
            rightdigit=kthDigit(n,i)
            leftdigit=kthDigit(n,dc-i)
            if rightdigit!=leftdigit:
                return False
        return True

def reversenum(n):
    newnum=0
    for i in range(digitCount(n)):
        newnum+=kthDigit(n,i)
        newnum=newnum*10
    return int(newnum/10)
def isLychrel(num1):
    for i in range(50):
        num2=reversenum(num1)
        num1=num1+num2
        if isPalindrome(num1):
            return True
    return False

lychrelcount=0
lychrels=[]
for i in range(10000):
    if isLychrel(i):
        lychrels.append(i)
        lychrelcount+=1
print(10000-lychrelcount)

