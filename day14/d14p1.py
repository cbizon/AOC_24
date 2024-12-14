from collections import defaultdict

class Robot:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def advance(self,nx,ny):
        self.x += self.vx
        self.x = self.x % nx
        self.y += self.vy
        self.y = self.y % ny

    def get_quadrant(self,nx,ny):
        print("position:",self.x, self.y)
        qx = (nx-1)/2
        qy = (ny-1)/2
        if self.x < qx:
            if self.y < qy:
                return 1
            if self.y > qy:
                return 3
        if self.x > qx:
            if self.y < qy:
                return 2
            if self.y > qy:
                return 4
        return 0

def read_input(infile):
    robots = []
    with open(infile) as f:
        for line in f:
            p = line.strip().split()
            position = p[0].split("=")[1]
            xy = position.split(',')
            x = int(xy[0])
            y = int(xy[1])
            velocity = p[1].split("=")[1]
            vxvy = velocity.split(',')
            vx = int(vxvy[0])
            vy = int(vxvy[1])
            r = Robot(x,y,vx,vy)
            robots.append(r)
    return robots

def score(robots,nx,ny):
    robot_count = defaultdict(int)
    for r in robots:
        q = r.get_quadrant(nx,ny)
        print("quadrant:", q)
        if not q == 0:
            robot_count[q] += 1
    safety = 1
    for q in range(1,5):
        print(q,robot_count[q])
        safety *= robot_count[q]
    return safety

def go():
    # test values
    #fname = "testinput.txt"
    #nx = 11
    #ny = 7
    #real values
    fname = "input.txt"
    nx = 101
    ny = 103
    # and begin
    rs = read_input(fname)
    for step in range(100):
        for robot in rs:
            robot.advance(nx,ny)
    n = score(rs,nx,ny)
    print("score:",n)

if __name__ == "__main__":
    go()