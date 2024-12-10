import math

l1 = []
l2 = []
with open("p1_input.txt","r") as inf:
    for line in inf:
        x = line.strip().split()
        l1.append(int(x[0]))
        l2.append(int(x[-1]))

l1.sort()
l2.sort()

diffs = [math.fabs( n-m ) for n,m in zip(l1,l2)]
print(l1[:4])
print(l2[:4])
print(diffs[:4])
print(sum(diffs))
