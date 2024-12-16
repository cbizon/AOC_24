#This is not particularly good, but it does work. The idea is quite similar to day 1 - we move the robot
# and it hits other objects and tries to move them. If they can't move then they report back up the chain.
# the difference here is that you can have cases where one block can push on two blocks, and one of those hits a wall
# and the other doesn't.  So you can't have the blocks move yet, because we need to aggregate that information back
# all the way up, and then pass it back down.

# So the plan - push, collect provisional movements, aggregate back up at the robot, and then push back down
# a signal saying whether to implement or flush the provisional movement

import numpy as np

class Obstacle:
    def __init__(self, pos, kind):
        #the pos here is the left of the two positions
        self.kind = kind
        self.positions = [ pos ]
        if kind != "@":
            rpos = pos + np.array((1,0), dtype=int)
            self.positions.append(rpos)
        self.in_provisional_state = False
        self.bumpers = [ ]
        self.provisional_positions = []
        self.scored = False
    def push(self, d, obstacles):
        #Can't push a wall
        if self.kind == "#":
            return False
        if self.in_provisional_state:
            return self.could_move
        #where are we trying to go:
        newpos = [p + d for p in self.positions]
        tnewpos = [tuple(np) for np in newpos]
        bumping = []
        for newp in tnewpos:
            if newp in obstacles:
                o = obstacles[newp]
                if o != self and o not in bumping:
                    bumping.append(o)
        moved = True
        for b in bumping:
            moved = moved and b.push(d, obstacles)
        #either we moved the obstacle or there wasn't one
        self.provisional_update(newpos,bumping,moved)
        return moved
    def provisional_update(self, newpos, b, moved):
        self.provisional_newpos = newpos
        #these are the obstacles we need to notify if a move actually happens
        self.bumpers = b
        #is this provisional move allowed by the neighbors?
        self.could_move = moved
        self.in_provisional_state = True
    def update(self, execute, obstacles):
        if not self.in_provisional_state:
            return
        # if execute is False, then we hit an obstacle somewhere, so flush the provisional stuff
        self.in_provisional_state = False
        if not execute:
            for b in self.bumpers:
                b.update(execute, obstacles)
            self.provisonal_newpos = []
            self.bumpers = []
            return
        for b in self.bumpers:
            b.update(execute,obstacles)
        # if it's a boulder, change obstacles
        if self.kind == "O":
            tpos = [tuple(p) for p in self.positions]
            for tp in tpos:
                del obstacles[tp]
            for p in self.provisional_newpos:
                obstacles[tuple(p)] = self
        # move
        self.positions = self.provisional_newpos
        self.provisional_newpos = []
        self.bumpers = []
    def score(self):
        if self.kind == "#":
            return 0
        if self.scored:
            return 0
        mx = min( [p[0] for p in self.positions] )
        my = min( [p[1] for p in self.positions] )
        s = 100*my + mx
        self.scored = True
        return s

def read_input(infile):
    #We'll use a coordinate system where 0,0 is the top left, and x increases to the right and y down.
    # so our directions are
    ds = {"^": np.array((0,-1), dtype=int),
          ">": np.array((1,0), dtype=int),
          "v": np.array((0,1), dtype=int),
          "<": np.array((-1,0), dtype=int)}
    objects = {}
    directions = []
    with open(infile) as f:
        mode = "map"
        for y,line in enumerate(f):
            l = line.strip()
            if len(l) == 0:
                mode = "moves"
                continue
            if mode == "map":
                for x,c in enumerate(l):
                    xobj = x * 2
                    if c == ".":
                        continue
                    pos = np.array((xobj,y),dtype=int)
                    o = Obstacle(pos, c)
                    if c == "@":
                        robot = o
                    else:
                        objects[tuple(pos)] = o
                        rpos = pos + (np.array((1,0), dtype = int))
                        objects[tuple(rpos)] = o
            else:
                for c in l:
                    directions.append( ds[c] )
    return robot, objects, directions

def draw_thing(objects,robot):
    rpos = tuple(robot.positions[0])
    maxx = 100
    maxy = 50
    for y in range(maxy):
        line = []
        for x in range(maxx):
            if (x,y) in objects:
                line.append(objects[(x,y)].kind)
            elif (x,y) == rpos:
                line.append("@")
            else:
                line.append(".")
        print(''.join(line))
    print("")

def go():
    robot, objects, directions = read_input("input.txt")
    for step in directions:
        nobj = len(objects)
        moved = robot.push(step,objects)
        robot.update(moved,objects)

        #For debugging
        #print(robot.positions)
        #draw_thing(objects, robot)

        #This bit of code is to catch the kinds of errors that I was having
        if not len(objects) == nobj:
            print(f"there should be {nobj} but instead are {len(objects)}")
            print(len(objects))
            break

    total = 0
    for o in objects.values():
        total += o.score()
    print(total)

if __name__ == "__main__":
    go()