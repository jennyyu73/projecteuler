#43 substring divisibility
def kthDigit(n,k):
    return (abs(n)//10**k)%10
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
def isPandigital(n):
    temp=abs(n)
    for i in range (0,10,1):
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

pandigitalsum=0

def buildnum(d1,d2,d3, num):
    num=0
    if (kthDigit(num,d1))!=0:
        num+=kthDigit(num,d1)
        num=num*10
    num+=kthDigit(num,d2)
    num=num*10
    num+=kthDigit(num,d3)
    return num

for i in range(1234567890,9876543210):
    if (buildnum(2,3,4,i)%2)==0:
        if (buildnum(3,4,5,i)%3)==0:
            if (buildnum(4,5,6,i)%5)==0:
                pandigitalsum+=i
print("okay")

                             
