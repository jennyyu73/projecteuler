#project euler 56 powerful digit sum

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
maxdigitsum=0
for a in range(1,101):
    for b in range(1,101):
        digitsum=0
        num=a**b
        for i in range(digitCount(num)):
            digitsum+=kthDigit(num,i)
        if digitsum>maxdigitsum:
            maxdigitsum=digitsum
print(maxdigitsum)

end=time.time()
print(end-start,"seconds")
