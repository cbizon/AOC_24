from collections import defaultdict
from copy import deepcopy

def read_input(fname):
    map = []
    with open(fname) as f:
        for line in f:
            map.append([int(x) for x in line.strip()])
    return map

def find(map, n):
    ns = []
    for i,line in enumerate(map):
        for j,x in enumerate(line):
            if x == n:
                ns.append( (i,j) )
    return ns

def create_path_segments(map):
    downhills = defaultdict(list)
    for i in range(len(map)):
        for j in range(len(map[i])):
            current_height = map[i][j]
            for diff in [(0,1), (1,0), (-1,0), (0,-1)]:
                try:
                    there = (i+diff[0], j+diff[1])
                    if there[0] >= 0 and there[1] >= 0 and there[0] < len(map) and there[1] < len(map[0]):
                        if map[there[0]][there[1]] == current_height-1:
                            downhills[(i,j)].append(there)
                except:
                    #FWIW, this no longer gets hit.  The try/except is a failed approach because indexing with -1 is allowed (ugh)
                    #out of bounds
                    pass
    return downhills

def walk_downhill(nines, downhills, npaths):
    next = set()
    for n in nines:
        next.add(n)
    s = 1
    while len(next) > 0:
        print("step",s)
        s+=1
        newnext = set()
        for n in next:
            for step in downhills[n]:
                newnext.add(step)
                npaths[step]+=npaths[n]
        next = newnext
    return npaths

def go():
    input = read_input("input.txt")
    downhills = create_path_segments(input)
    nines = find(input,9)
    npaths = defaultdict(int) #how many paths
    for n in nines:
        npaths[n] = 1
    npaths = walk_downhill(nines, downhills, npaths)
    trailheads = find(input, 0)
    total = 0
    for th in trailheads:
        total += npaths[th]
    print(total)

if __name__ == "__main__":
    go()