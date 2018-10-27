#113 non-bouncy numbers
def kthDigit(n,k):
    return (abs(n)//10**k)%10
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
def isIncreasing(n):
    for i in range(digitCount(n)-1):
        if kthDigit(n,i)<kthDigit(n,i+1):
            return False
    return True
def isDecreasing(n):
    for i in range(digitCount(n)-1):
        if kthDigit(n,i)>kthDigit(n,i+1):
            return False
    return True

nonbounce=99

for i in range(100,10**100):
    if isIncreasing(i) or isDecreasing(i):
        nonbounce+=1
print(nonbounce)
