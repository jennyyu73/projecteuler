#9 special pythagorean triplet
import time
start=time.time()
a=0
b=0
c=0

while a+b+c!=1000 or a+b+c<1000:
    for m in range(500):
        for n in range(500):
            a=m**2-n**2
            b=2*m*n
            c=m**2+n**2
print(a*b*c)
end=time.time()
print(end-start,"seconds")
