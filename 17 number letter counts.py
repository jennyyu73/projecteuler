#Number letter counts

def digitCount(n):
    digitcounter=0
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter

def kthDigit(n,k):
    return (abs(n)//10**k)%10

def tens(n):
    if n==0:
        return ""
    if n==2:
        return "twenty"
    if n==3:
        return "thirty"
    if n==4:
        return "forty"
    if n==5:
        return "fifty"
    if n==6:
        return "sixty"
    if n==7:
        return "seventy"
    if n==8:
        return "eighty"
    if n==9:
        return "ninety"

def tensrevised(n):
    if n==0:
        return "ten"
    if n==2:
        return "twelve"
    if n==3:
        return "thirteen"
    if n==4:
        return "fourteen"
    if n==5:
        return "fifteen"
    if n==6:
        return "sixteen"
    if n==7:
        return "seventeen"
    if n==8:
        return "eighteen"
    if n==9:
        return "nineteen"

def ones(n):
    if n==0:
        return ""
    if n==1:
        return "one"
    if n==2:
        return "two"
    if n==3:
        return "three"
    if n==4:
        return "four"
    if n==5:
        return "five"
    if n==6:
        return "six"
    if n==7:
        return "seven"
    if n==8:
        return "eight"
    if n==9:
        return "nine"

def hundreds(n):
    if n==0:
        return ""
    if n==1:
        return "onehundredand"
    if n==2:
        return "twohundredand"
    if n==3:
        return "threehundredand"
    if n==4:
        return "fourhundredand"
    if n==5:
        return "fivehundredand"
    if n==6:
        return "sixhundredand"
    if n==7:
        return "sevenhundredand"
    if n==8:
        return "eighthundredand"
    if n==9:
        return "ninehundredand"


count=0
for i in range(1,20): #go from 1 to 999, add 11 in the end for one thousand
    num=""
    length=digitCount(i)
    for k in range(length):
        if k==0 and kthDigit(i,k+1)!=1:
            word=ones(kthDigit(i,k))
            num+=word
        if k==1 and kthDigit(i,k)!=1:
            word=tens(kthDigit(i,k))
            num+=word
        if k==1 and kthDigit(i,k)==1:
            word=tensrevised(kthDigit(i,k-1))
            num+=word
        if k==2:
            word=hundreds(kthDigit(i,k))
            num+=word
        
print(len(str(num))+11)   
