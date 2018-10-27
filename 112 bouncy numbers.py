#112 bouncy numbers
import time
start=time.time()
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
potentialbounce=99
bouncecount=0

while (bouncecount*100)<(potentialbounce*99):
    potentialbounce+=1
    if isDecreasing(potentialbounce)==False and isIncreasing(potentialbounce)==False:
        bouncecount+=1
print(potentialbounce)
end=time.time()
print(end-start,"seconds")

