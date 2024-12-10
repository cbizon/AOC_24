from collections import defaultdict

l1 = []
d2 = defaultdict(int)
with open("p1_input.txt","r") as inf:
    for line in inf:
        x = line.strip().split()
        l1.append(int(x[0]))
        d2[int(x[-1])] += 1

sim = 0
for n in l1:
    sim += d2[n]*n

print(sim)
