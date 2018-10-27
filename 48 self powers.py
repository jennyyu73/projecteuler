#48 self powers

def kthDigit(n,k):
    return (abs(n)//10**k)%10

selfsum=0
for i in range(1,1001):
    selfsum+=i**i

tendigits=0
for i in range(10):
    tendigits=tendigits+kthDigit(selfsum,i)*10**i
    tendigits+=10
print(tendigits)
    
