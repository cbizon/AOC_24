from collections import defaultdict
#I guess dijkstra isn't really needed here, since the path is only just a path

def read_input(infile):
    # reading like this indexes with (y,x) duh
    input = []
    with open(infile) as f:
        for line in f:
            if 'S' in line:
                start_x = line.index("S")
                start_y = len(input)
            input.append( line.strip() )
    transpose = []
    for i in range(len(input[0])):
        transpose.append([])
    for i,row in enumerate(input):
        for j,char in enumerate(row):
            transpose[j].append(char)
    return transpose, (start_x, start_y)

def handle_step(last, current, borders, map):
    # 1) finds the next step, which is the bordering . that we didnt' come from
    # 2) Finds all the places we could go through by cheating (the borders)
    for dx,dy in [ (-1,0), (0,1), (0,-1), (1,0) ]:
        nx = current[0] + dx
        ny = current[1] + dy
        if (nx,ny) == last:
            # this is the direction we came from
            continue
        char = map[nx][ny]
        if char in [".", "E"]:
            next = (nx,ny)
        elif char == "#":
            borders[ (nx,ny) ].append(current)
    if map[current[0]][current[1]] == 'E':
        return None
    return next

def walk(track, start ):
    current = start
    last = start
    times = {}
    borders = defaultdict(list)
    step = 0
    times[current] = step
    next = "?"
    while next is not None:
        times[current] = step
        step += 1
        next = handle_step(last, current, borders, track)
        last = current
        current = next
    print(f"We made it to the end {current} in {step}")
    return borders,times

def ab(x):
    if x >=0:
        return x
    return -x

def evaluate(x,y,themap,times,max_x, max_y, delta = 20):
    savings = defaultdict(list)
    if themap[x][y] == "#":
        return savings
    start_t = times[ (x,y) ]
    for dx in range(-delta, delta+1):
        if x+dx < 0:
            continue
        if x+dx >= max_x:
            continue
        adx = ab(dx)
        for dy in range(-(delta-adx), delta-adx+1):
            if y+dy < 0:
                continue
            if y+dy >= max_y:
                continue
            #Now we have 2 points, x,y and x+dx,y+dy that are both in the grid and close to each other
            if themap[x+dx][y+dy] == "#":
                continue
            end_t = times[ (x+dx, y+dy) ]
            s = end_t - start_t - adx - ab(dy)
            #if s == 79:
            #    print(x,y, dx,dy, adx,ab(y),end_t,start_t)
            if end_t > start_t:
                savings[s].append( ((x,y), (x+dx, y+dy)) )
    return savings

def find_savings(times, themap, cutoff=100):
    # for every point in the times, look at all other points within that distance, find the time delta
    max_x = len(themap[0])
    max_y = len(themap)
    total_savings = defaultdict(list)
    for y in range(max_y):
        for x in range(max_x):
            # Evaluate this point: x,y
            point_savings = evaluate(x,y,themap,times,max_x, max_y)
            for s in point_savings:
                total_savings[s] += point_savings[s]
    return total_savings

def go():
    cutoff = 100
    input,start = read_input("input.txt")
    _, times = walk(input,start)
    # the walls approach doesn't really work here.  Instead, we should be looking at any reachable spot within 20 (manhattan) distance
    savings = find_savings(times,input)
    n = 0
    pres = []
    for saving, cheats in savings.items():
        if saving >= cutoff:
            pres.append( (saving,len(cheats)))
            n += len(cheats)
    print(n)
    #pres.sort()
    #for s,c in pres:
    #    print(f"There are {c} cheats that save {s}")

if __name__ == "__main__":
    go()