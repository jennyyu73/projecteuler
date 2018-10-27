#Euler 40: Champernowne's constant
import time
start=time.time()
def digitCount(n):
    digitcounter=0
    if n==0:return 1  # I fixed this
    n=abs(n)
    while n//10!=n:
        digitcounter=digitcounter+1
        n=n//10
    return digitcounter
num=0
for i in range (1,200000):
    num=num*10**digitCount(i)
    num+=i
end=time.time()
print(end-start,"seconds")
num=str(num)
#length of num is 1088889
product=int(num[0])*int(num[9])*int(num[99])*int(num[999])*int(num[9999])*int(num[99999])*int(num[999999])
