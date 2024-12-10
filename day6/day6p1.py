import numpy as np

def read_input(infile):
    obs = set()
    with open(infile) as inf:
        row = 0
        for line in inf:
            ncols = len(line)
            for col,val in enumerate(line):
                if val == '#':
                    obs.add( (row,col) )
                if val == "^":
                    guard = np.array((row,col),dtype=int)
            row += 1
    return obs, guard, row, ncols

def is_outside(loc,nrows,ncols):
    return loc[0] < 0 or loc[0] >= nrows or loc[1] < 0 or loc[1] >= ncols

def turn_right(gv):
    if (gv == np.array([-1,0])).all():
        return np.array([0,1],dtype=int)
    if (gv == np.array([0,1])).all():
        return np.array([1,0],dtype=int)
    if (gv == np.array([1,0])).all():
        return np.array([0,-1],dtype=int)
    if (gv == np.array([0,-1])).all():
        return np.array([-1,0],dtype=int)
    print("error")
    return None

def go():
    walked=set()
    obs, guard, nrows, ncols = read_input("input.txt")
    guard_v = np.array([-1,0],dtype=int)
    inside = True
    while inside:
        walked.add( tuple(guard) )
        newloc = guard + guard_v
        if is_outside(newloc,nrows,ncols):
            print("Outside", newloc)
            inside=False
        elif tuple(newloc) in obs:
            print("Hit", newloc)
            guard_v = turn_right(guard_v)
        else:
            guard = newloc
            print("moved to ", guard)
    print(len(walked))


if __name__ == "__main__":
    go()