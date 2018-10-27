import math
def kthDigit(n,k):
    return (abs(n)//10**k)%10

digitsum=0
for i in range(100,0,-1):
    if math.sqrt(i)!=int(math.sqrt(i)):
        num=math.sqrt(i)
        for k in range(101):
            print(num)
            digitsum+=kthDigit(num,0)
            num=num-kthDigit(num,0)
            num=num*10
print(digitsum)
