from copy import deepcopy
import heapq

def read_input(infile):
    # X is positive down, Y is positive to the right
    input = []
    with open(infile) as f:
        for line in f:
            input.append( line.strip() )
            y = line.find("S")
            if y >= 0:
                ys = y
                xs = len(input) - 1
            y = line.find("E")
            if y >= 0:
                ye = y
                xe = len(input) -1
    return input,xs,ys,xe,ye

class Point:
    def __init__(self,x,y,dx,dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.score = 0
        # We're using a heap for ordering. So when a score changes, we have to invalidate the old entry rather than remove it
        self.valid = True
    def __lt__(self, other):
        return self.score < other.score

def get_steps(themap,x,y,dx,dy):
    #returns a list of possible steps in the form
    # (new_x, new_y, new_dx, new_dy, delta_score)
    r = []
    # Can I take a step forward?
    nx = x + dx
    ny = y + dy
    if themap[nx][ny] != "#":
        r.append( (nx,ny,dx,dy,1) )
    #left turn
    ndx = dy
    ndy = -dx
    r.append((x, y, ndx, ndy,1000))
    # right turn
    ndx = -dy
    ndy = dx
    r.append((x, y, ndx, ndy,1000))
    return r

def dijkit(x_i,y_i,dx_i,dy_i,x_f,y_f,themap):
    # This started as a semi-dijkstra's algorithm, which turns out to mean a little like Dijkstra's algorithm
    # except that it doesn't work.  So fine, I looked up how it actually works.
    start = Point(x_i, y_i, dx_i, dy_i)

    heap_of_points = []
    heapq.heappush(heap_of_points,start)

    visited_points = set()
    unvisited_points = {} # from (x,y,dx,dy) to Point (with score)

    while True:
        # if a score changes, we invalidate the point, so we will be pulling invalid points to ignore
        found_valid_point = False
        while not found_valid_point:
            current_point = heapq.heappop(heap_of_points)
            found_valid_point = current_point.valid
        #print("Current shortest path location, direction, score=",shortest_path.current, shortest_path.score)
        current_score = current_point.score
        visited_points.add( (current_point.x, current_point.y, current_point.dx, current_point.dy ) )
        if current_point.x == x_f and current_point.y == y_f:
            print("Final score", current_score)
            break
        possible_steps = get_steps(themap,current_point.x,current_point.y,current_point.dx,current_point.dy)
        for nx,ny,ndx,ndy,dscore in possible_steps:
            if (nx,ny,ndx,ndy) in visited_points:
                # We need not worry about these
                continue
            new_score = current_score + dscore
            if (nx,ny,ndx,ndy) in unvisited_points:
                p = unvisited_points[ (nx,ny,ndx,ndy) ]
                if new_score < p.score:
                    #we found a faster way here, congrats to us! (this is what was wrong with v1.)
                    #need to fix heap now. Invalidate the old point and add a new one with the lower score
                    p.valid = False
                    newp = Point(nx,ny,ndx,ndy)
                    newp.score = new_score
                    heapq.heappush(heap_of_points, newp)
            else:
                # We,re adding a new point to unvisited (technically moving score Infinity to something finite)
                newp = Point(nx, ny, ndx, ndy)
                newp.score = new_score
                heapq.heappush(heap_of_points, newp)



def go():
    themap,start_x,start_y,finish_x,finish_y = read_input("input.txt")
    # Starts going to the right: dx=0, dy=1
    dijkit(start_x,start_y,0,1,finish_x,finish_y,themap)

if __name__ == "__main__":
    go()