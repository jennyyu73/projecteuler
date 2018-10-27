#30 digit fifth powers

def kthDigit(n,k):
    return (abs(n)//10**k)%10
def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
yes=[]
for i in range(10, 200000):
    digits=[]
    for k in range(digitCount(i)):
        digits.append(kthDigit(i,k))
    sumofdigitfifths=0
    for k in range(len(digits)):
        sumofdigitfifths+=digits[k]**5
    if sumofdigitfifths==i:
        yes.append(i)
print(sum(yes))
