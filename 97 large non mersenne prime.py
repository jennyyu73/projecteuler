#large non mersesnne prime 97

num=28433*2**(7830457)+1

def kthDigit(n,k):
    return (abs(n)//10**k)%10
digits=0
for i in range(9,-1,-1):
    digits=digits*10+kthDigit(num,i)
print(digits)
