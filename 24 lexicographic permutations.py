#24 lexicographic permutations

from itertools import permutations

lexipermutations=list(permutations([0,1,2,3,4,5,6,7,8,9]))
millionth=lexipermutations[999999]
millionthperm=0
for i in range(len(millionth)):
    millionthperm+=millionth[i]
    millionthperm=millionthperm*10
print(millionthperm//10)
