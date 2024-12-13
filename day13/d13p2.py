class Problem:
    # This is a just a 2x2 system of equations to solve
    def __init__(self, c_ax, c_ay, c_bx, c_by, p_x, p_y):
        self.c_ax = c_ax
        self.c_ay = c_ay
        self.c_bx = c_bx
        self.c_by = c_by
        self.p_x = p_x
        self.p_y = p_y
    def solve(self):
        self.na = (self.c_by * self.p_x - self.c_bx * self.p_y) / (self.c_ax * self.c_by - self.c_ay * self.c_bx)
        self.nb = ( self.p_y - self.c_ay * self.na ) / (self.c_by)
        #now, there are some constraints we want - only integer solutions between 0 and 100
        if self.na < 0 or self.na> 100 or self.nb < 0 or self.nb > 100:
            return None,None
        dec_a = self.na % 1
        dec_b = self.nb % 1
        tol = 0.001
        if dec_a > tol or dec_b > tol:
            return None,None
        return int(self.na), int(self.nb)

def read_input(infile):
    input = []
    with open(infile) as f:
        while True:
            line = f.readline().strip().split(' ')
            c_ax = int(line[2].split("+")[1][:-1])
            c_ay = int(line[3].split("+")[1])
            line = f.readline().strip().split(' ')
            c_bx = int(line[2].split("+")[1][:-1])
            c_by = int(line[3].split("+")[1])
            line = f.readline().strip().split(' ')
            p_x = int(line[1].split("=")[1][:-1])
            p_y = int(line[2].split("=")[1])
            input.append( Problem(c_ax, c_ay, c_bx, c_by, p_x, p_y) )
            line = f.readline()
            if line == '':
                break
    return input

def go():
    input = read_input("input.txt")
    cost = 0
    for problem in input:
        x,y = problem.solve()
        if x is not None:
            cost += 3*x + y
            print(x,y,cost)
    print("Total cost:",cost)

if __name__ == "__main__":
    go()