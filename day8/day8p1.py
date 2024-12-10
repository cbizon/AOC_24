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

def calc_from_pair(loc0, loc1):
    x0, y0 = loc0
    x1, y1 = loc1
    # this vector points from loc0 to loc1
    dx = x1 - x0
    dy = y1 - y0
    # There's a node subtracting dx and dy from loc0 and adding them to loc1
    a0x = x0 - dx
    a0y = y0 - dy
    a1x = x1 + dx
    a1y = y1 + dy
    return (a0x, a0y), (a1x, a1y)

def calculate_antinodes(locations):
    total_antis = set()
    for iloc, loc0 in enumerate(locations):
        for loc1 in locations[iloc+1:]:
            antis = calc_from_pair(loc0, loc1)
            total_antis.add(antis[0])
            total_antis.add(antis[1])
    return total_antis

def go():
    antennae, nrows, ncols = read_input("input.txt")
    print(antennae.keys(), nrows, ncols)
    all_antinodes=set()
    for atype in antennae:
        antinodes = calculate_antinodes(antennae[atype])
        for an in antinodes:
            if an[0] >= 0 and an[0] < nrows and an[1] >= 0 and an[1] < ncols:
                all_antinodes.add(an)
    print(len(all_antinodes))

if __name__ == "__main__":
    go()