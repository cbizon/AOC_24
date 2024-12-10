import numpy as np
from copy import deepcopy

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

def complete_walk(guard, guard_v, obs, nrows, ncols):
    walked=set()
    states=set()
    inside = True
    while inside:
        walked.add( tuple(guard) )
        newloc = guard + guard_v
        state = (tuple(newloc), tuple(guard_v))
        if state in states:
            #print("Loop", newloc)
            return "Loop"
        else:
            states.add(state)
        if is_outside(newloc,nrows,ncols):
            #print("Outside", newloc)
            inside=False
        elif tuple(newloc) in obs:
            #print("Hit", newloc)
            guard_v = turn_right(guard_v)
        else:
            guard = newloc
            #print("moved to ", guard)
    return walked

def go():
    obs, original_guard, nrows, ncols = read_input("input.txt")
    guard_v = np.array([-1,0],dtype=int)
    walked = complete_walk(deepcopy(original_guard), guard_v, obs, nrows, ncols)
    # walked now containes all the places where we might want to try an obstacle
    print(len(walked))
    nloops = 0
    nchecked = 0
    for new_hash in walked:
        new_obs = deepcopy(obs)
        new_obs.add( tuple(new_hash) )
        r = complete_walk(deepcopy(original_guard), guard_v, new_obs, nrows, ncols)
        if r == "Loop":
            print("Loop at", new_hash)
            nloops += 1
        print (f"{nloops} / {nchecked}")
    print(nloops)


if __name__ == "__main__":
    go()