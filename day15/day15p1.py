import numpy as np

class Obstacle:
    def __init__(self, pos, kind):
        self.kind = kind
        self.pos = pos
    def push(self, d, obstacles):
        #Can't push a wall
        if self.kind == "#":
            return False
        #where are we trying to go:
        newpos = self.pos + d
        tnewpos = tuple(newpos)
        if tnewpos in obstacles:
            moved = obstacles[tnewpos].push(d, obstacles)
            if not moved:
                return False
        #either we moved the obstacle or there wasn't one
        self.update(newpos,obstacles)
        return True
    def update(self, newpos, obstacles):
        # if it's a boulder, change obstacles
        if self.kind == "O":
            t = tuple(self.pos)
            del obstacles[t]
            obstacles[tuple(newpos)] = self
        # move
        self.pos = newpos
    def score(self):
        if self.kind == "#":
            return 0
        s = 100*self.pos[1] + self.pos[0]
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
                    if c == ".":
                        continue
                    pos = np.array((x,y),dtype=int)
                    o = Obstacle(pos, c)
                    if c == "@":
                        robot = o
                    else:
                        objects[tuple(pos)] = o
            else:
                for c in l:
                    directions.append( ds[c] )
    return robot, objects, directions

def go():
    robot, objects, directions = read_input("input.txt")
    for step in directions:
        moved = robot.push(step,objects)
    total = 0
    for o in objects.values():
        total += o.score()
    print(total)

if __name__ == "__main__":
    go()