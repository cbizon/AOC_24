# this seems pretty similar to the dijkstra algorithm one from a few days ago except you don't pay for turning.

import heapq

def read_input(infile,nread):
    # X is positive right, Y is positive down
    input = set()
    with open(infile) as f:
        for line in f:
            x = line.strip().split(',')
            input.add( (int(x[0]), int(x[1]) ) )
            if len(input) >= nread:
                break
    print(len(input))
    return input

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.score = 0
        # We're using a heap for ordering. So when a score changes, we have to invalidate the old entry rather than remove it
        self.valid = True
        self.path = set( [(x,y)] )
    def __lt__(self, other):
        return self.score < other.score

def get_steps(themap,x,y,max_x,max_y):
    #returns a list of possible steps in the form
    # (new_x, new_y, new_dx, new_dy, delta_score)
    r = []
    for dx,dy in [ (-1,0), (0,1), (0,-1), (1,0) ]:
        nx = x + dx
        ny = y + dy
        if (nx,ny) in themap:
            continue
        if nx < 0 or nx > max_x:
            continue
        if ny < 0 or ny > max_y:
            continue
        r.append( (nx,ny,1) )
    return r

def drawit(themap, visited_points, current_point, mx, my):
    nblock = 0
    npath = 0
    for y in range(my+1):
        line=[]
        for x in range(mx+1):
            if (x,y) in themap:
                line.append("#")
                nblock+= 1
            elif (x,y) in current_point.path:
                line.append("o")
                npath += 1
            elif x == current_point.x and y == current_point.y:
                line.append("X")
            elif x == mx and y == my:
                line.append("E")
            else:
                line.append(" ")
        print(f"{''.join(line)}")
    print("Number of blocks", nblock)
    print("number of path points", npath)

def dijkit(x_i,y_i,x_f,y_f,themap):
    # Slightly modified from day 16, direction is no longer a relevant thing
    start = Point(x_i, y_i)

    heap_of_points = []
    heapq.heappush(heap_of_points,start)

    visited_points = set()
    unvisited_points = {} # from (x,y,dx,dy) to Point (with score)

    iteration = 0
    while True:
        iteration += 1
        # if a score changes, we invalidate the point, so we will be pulling invalid points to ignore
        found_valid_point = False
        while not found_valid_point:
            current_point = heapq.heappop(heap_of_points)
            found_valid_point = current_point.valid
        if (current_point.score != len(current_point.path) - 1):
            print("heey1!!")
            print(current_point.x, current_point.y)
            print(current_point.score, len(current_point.path))
            exit()
        #if iteration % 2000 == 0:
        #    print("Current shortest path location,  score=",current_point.x, current_point.y, current_point.score)
        #    exit()
        current_score = current_point.score
        visited_points.add( (current_point.x, current_point.y) )
        if current_point.x == x_f and current_point.y == y_f:
            drawit(themap,visited_points,current_point,x_f,y_f)
            print("Final score", current_score)
            break
        possible_steps = get_steps(themap,current_point.x,current_point.y,x_f,y_f) #the final is the bottom right
        for nx,ny,dscore in possible_steps:
            debug = False
            if nx == 14 and ny == 1:
                debug = True
                print(f"{nx}, {ny}, {dscore} in possible_steps")
                print(f"Current: {current_point.x}, {current_point.y}")
            if (nx,ny) in visited_points:
                # We need not worry about these
                if debug:
                    print("in visited")
                continue
            new_score = current_score + dscore
            if (nx,ny) in unvisited_points:
                p = unvisited_points[ (nx,ny) ]
                if debug:
                    print(f"in unvisited. score={p.score}")
                if new_score < p.score:
                    if debug:
                        print("but we have a better score")
                    #we found a faster way here, congrats to us! (this is what was wrong with v1.)
                    #need to fix heap now. Invalidate the old point and add a new one with the lower score
                    p.valid = False
                    newp = Point(nx,ny)
                    newp.path.update(current_point.path)
                    newp.score = new_score
                    heapq.heappush(heap_of_points, newp)
            else:
                # We,re adding a new point to unvisited (technically moving score Infinity to something finite)
                newp = Point(nx, ny)
                newp.score = new_score
                newp.path.update(current_point.path)
                unvisited_points[(nx, ny)] = newp
                heapq.heappush(heap_of_points, newp)



def go():
    #Test
    #start_x = 0
    #start_y = 0
    #finish_x = 6
    #finish_y = 6
    themap = read_input("testinput.txt",12)
    #Real
    start_x = 0
    start_y = 0
    finish_x = 70
    finish_y = 70
    themap = read_input("input.txt",1024)
    #run
    dijkit(start_x,start_y,finish_x,finish_y,themap)

if __name__ == "__main__":
    go()