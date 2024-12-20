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

def look_for_holes(walls,times):
    group_by_saving = defaultdict(list)
    for wall,paths in walls.items():
        if len(paths) > 3:
            print(wall)
            print("well then")
            exit()
        elif len(paths) < 2:
            continue
        for i,p0 in enumerate(paths):
            for p1 in paths[i+1:]:
                start = p0
                end = p1
                start_t = times[start]
                end_t = times[end]
                if end_t < start_t:
                    print("uck")
                    exit()
                savings = end_t - start_t - 2
                group_by_saving[savings].append(wall)
    return group_by_saving

def go():
    input,start = read_input("input.txt")
    walls, times = walk(input,start)
    savings = look_for_holes(walls,times)
    n = 0
    for saving, cheats in savings.items():
        if saving >= 100:
            n += len(cheats)
    print(n)

if __name__ == "__main__":
    go()