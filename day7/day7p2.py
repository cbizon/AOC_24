from itertools import product
from operator import mul, add

def cat(x,y):
    return int(str(x) + str(y))

def solve(line):
    x = line.strip().split(":")
    result = int(x[0])
    inputs = [ int(q) for q in x[1].split() ]
    n_ops = len(inputs) - 1
    for ops in product([mul, add, cat], repeat=n_ops):
        v = inputs[0]
        for i in range(n_ops):
            v = ops[i](v,inputs[i+1])
            if v > result:
                break
        if v == result:
            return v
    #print("No match")
    return 0

def go():
    with open("input.txt") as inf:
        working_values = 0
        for line in inf:
            working_values += solve(line)
    print(working_values)

if __name__ == "__main__":
    go()