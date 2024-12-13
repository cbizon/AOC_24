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

def count_exterior_corners(cell, region):
    # There's an exterior corner in the top left if the cell above AND the cell to the left are both not in the region
    corners = 0
    for dy in [-1,1]:
        c1 = (cell[0]+dy,cell[1])
        for dx in [-1,1]:
            c2 = (cell[0],cell[1]+dx)
            if not (c1 in region or c2 in region):
                corners += 1
    return corners

def count_interior_corners(cell, region):
    # There's an exterior corner in the top left if the cell above is not in the region but the cell to the left
    # and the cell up and to the left both are
    # I think that this is the ugliest thing ever but I don't see a nice way to handle it and at least this is explicit
    left = (cell[0],cell[1]-1)
    top = (cell[0]-1,cell[1])
    right = (cell[0],cell[1]+1)
    bottom = (cell[0]+1,cell[1])
    topleft = (cell[0]-1,cell[1]-1)
    top_right = (cell[0]-1,cell[1]+1)
    bottom_left = (cell[0]+1,cell[1]-1)
    bottom_right = (cell[0]+1,cell[1]+1)
    corners = 0
    if top not in region:
        if left in region and topleft in region:
            corners += 1
        if right in region and top_right in region:
            corners += 1
    if right not in region:
        if top in region and top_right in region:
            corners += 1
        if bottom in region and bottom_right in region:
            corners += 1
    if bottom not in region:
        if left in region and bottom_left in region:
            corners += 1
        if right in region and bottom_right in region:
            corners += 1
    if left not in region:
        if top in region and topleft in region:
            corners += 1
        if bottom in region and bottom_left in region:
            corners += 1
    return corners

def count_region_corners(cells):
    ecorners = 0
    icorners = 0
    for cell in cells:
        ecorners += count_exterior_corners(cell,cells)
        icorners += count_interior_corners(cell,cells)
    # icorners will be found by both bordering cells, so divide by 2
    return ecorners + icorners / 2

def go():
    input = read_input("input.txt")
    #The region map is an array with the same dimensions as input,
    # initialized to all zeros (no region)
    regions,fence_counts = assign_regions(input)
    areas = defaultdict(set)
    total = 0
    for i,rline in enumerate(regions):
        for j,r in enumerate(rline):
            areas[r].add((i,j))
    for region in areas:
        # The number of edges is the number of corners
        corners = count_region_corners(areas[region])
        total += corners * len(areas[region])
    #for my input it should be 855082
    print(total)


if __name__ == "__main__":
    go()