from collections import defaultdict

def read_input(infile):
    input = []
    with open(infile) as f:
        for line in f:
            input.append( [i for i in line.strip() ] )
    return input

def make_region_map(input):
    regions = []
    for row in input:
        regions.append( [] )
        for char in row:
            regions[-1].append(0)
    return regions

def neighbor_positions(i,j,field):
    np = []
    for dx,dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        np.append((i+dx, j+dy))
    return np

def expand_region(regions, field, fence_count, i, j, crop):
    region = regions[i][j]
    current_positions = [(i,j)]
    min_x = 0
    min_y = 0
    max_x = len(field)-1
    max_y = len(field[0]) - 1
    n = 0
    while len(current_positions) > 0:
        n+=1
        next_positions = set()
        # evaluate the current position
        for c_i, c_j in current_positions:
            nps = neighbor_positions(c_i,c_j,field)
            for n_x, n_y in nps:
                if n_x >= min_x and n_x <= max_x and n_y >= min_y and n_y <= max_y:
                    # if the neighbor is a different crop add a fence
                    if field[n_x][n_y] != crop:
                        fence_count[c_i][c_j] += 1
                    else:
                        # same crop it better be either the same region or 0
                        if regions[n_x][n_y] == 0:
                            regions[n_x][n_y] = region
                            next_positions.add( (n_x, n_y) )
                else:
                    fence_count[c_i][c_j] += 1

        current_positions = next_positions


def assign_regions(field):
    # this is one approach where we basically expand the regions in a breadth first way
    # I think that there's a perhaps more satisfying / elegant approach where you build a connectivity map up
    # and to the left, then walk that dictionary to create regions.  But maybe we'll do that later...
    regions = make_region_map(field)
    fence_count = make_region_map(field)
    next_region = 1
    for i,line in enumerate(field):
        for j,crop in enumerate(line):
            if regions[i][j] == 0:
                regions[i][j] = next_region
                expand_region(regions, field, fence_count, i, j, crop)
                next_region +=1
    return regions, fence_count

def go():
    input = read_input("input.txt")
    #The region map is an array with the same dimensions as input,
    # initialized to all zeros (no region)
    regions,fence_counts = assign_regions(input)
    areas = defaultdict(int)
    perimeters = defaultdict(int)
    for i,rline in enumerate(regions):
        for j,r in enumerate(rline):
            areas[r] += 1
            perimeters[r] += fence_counts[i][j]

    total = 0
    for r in areas:
        total +=  areas[r]*perimeters[r]
        #print(r, areas[r], perimeters[r], total)
    print(total)

if __name__ == "__main__":
    go()