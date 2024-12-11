# The story leads you astray with this line business.  The order
# doesn't matter. So use a dict to cut down on repeated calculations

from collections import defaultdict

def read_input(infile):
    input = defaultdict(int)
    with open(infile) as f:
        line = f.readline().strip().split()
        for i in line:
            input[int(i)] += 1
    return input

def update_stone(input_stone):
    if input_stone == 0:
        return [1]
    s = str(input_stone)
    if len(s) % 2 == 0:
        n_dig = len(s) // 2
        return [ int(s[:n_dig]), int(s[n_dig:]) ]
    return [ 2024 * input_stone ]

def update(stones):
    newstones = defaultdict(int)
    for oldstone,oldstonecount in stones.items():
        for stone in update_stone(oldstone):
            newstones[stone] += oldstonecount
    return newstones

def go(num_iter=25):
    stones = read_input("input.txt")
    print(input)
    for i in range(num_iter):
        stones = update(stones)
        print(i, sum(stones.values()))

if __name__ == "__main__":
    #part 1
    #go(25)
    #part 2 - doesn't work, too slow
    go(75)
