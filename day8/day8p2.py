from collections import defaultdict

def read_input(infile):
    antennae = defaultdict(list)
    with open(infile) as inf:
        row = 0
        for line in inf:
            line = line.strip()
            ncols = len(line)
            for col,val in enumerate(line):
                if val != '.':
                    antennae[val].append( (row,col) )
            row += 1
    return antennae, row, ncols

def in_grid(x,y,nrows, ncols):
    if x >= 0 and x < nrows and y >= 0 and y < ncols:
        return True
    return False

def calc_from_pair(loc0, loc1,nrows, ncols):
    x0, y0 = loc0
    x1, y1 = loc1
    # this vector points from loc0 to loc1
    dx = x1 - x0
    dy = y1 - y0
    antis = []
    # There's a node subtracting dx and dy from loc0 and adding them to loc1
    a0x = x0
    a0y = y0
    while in_grid(a0x, a0y, nrows, ncols):
        antis.append( (a0x, a0y) )
        a0x -= dx
        a0y -= dy
    a1x = x1
    a1y = y1
    while in_grid(a1x, a1y, nrows, ncols):
        antis.append( (a1x, a1y) )
        a1x += dx
        a1y += dy
    return antis

def calculate_antinodes(locations,nrows,ncols):
    total_antis = set()
    for iloc, loc0 in enumerate(locations):
        for loc1 in locations[iloc+1:]:
            antis = calc_from_pair(loc0, loc1,nrows,ncols)
            total_antis.update(antis)
    return total_antis

def go():
    antennae, nrows, ncols = read_input("input.txt")
    all_antinodes=set()
    for atype in antennae:
        antinodes = calculate_antinodes(antennae[atype],nrows,ncols)
        #print(atype,len(antinodes))
        all_antinodes.update(antinodes)
    print(len(all_antinodes))

if __name__ == "__main__":
    go()