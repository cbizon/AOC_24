def read_input(infile):
    with open(infile) as f:
        line = f.readline()
        input = [int(i) for i in line.strip().split()]
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
    newstones = []
    for stone in stones:
        newstones += update_stone(stone)
    return newstones

def go(num_iter=25):
    stones = read_input("input.txt")
    print(input)
    for i in range(num_iter):
        stones = update(stones)
        print(i, len(stones))

if __name__ == "__main__":
    #part 1
    go(25)
    #part 2 - doesn't work, too slow
    #go(75)
