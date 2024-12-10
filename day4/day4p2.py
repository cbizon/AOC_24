import numpy

def read_input(infname):
    puzzle_input = []
    with open(infname) as f:
        for line in f:
            puzzle_input.append([x for x in line.strip()])
    return puzzle_input

def check(lines, i, j):
    if lines[i][j] != "M":
        return 0
    if lines[i+1][j+1] != "A":
        return 0
    if lines[i][j+2] != "S":
        return 0
    if lines[i+2][j] != "M":
        return 0
    if lines[i+2][j+2] != "S":
        return 0
    return 1

def count_all(lines):
    total = 0
    for i in range(len(lines)-2):
        for j in range(len(lines[0])-2):
            total += check(lines,i,j)
    return total

def invert(lines):
    newlines = []
    for line in lines:
        newlines.append(line[::-1])
    return newlines

def transpose(lines):
    return numpy.transpose(lines)

def go():
    puzzle_input = read_input("input.txt")
    nleft_right = count_all(puzzle_input)
    new_input = invert(puzzle_input)
    nright_left = count_all(new_input)
    tpose = transpose(puzzle_input)
    ntop_bottom = count_all(tpose)
    new_input = invert(tpose)
    nbottom_top = count_all(new_input)
    print(nleft_right, nright_left, ntop_bottom, nbottom_top)
    print(nleft_right + nright_left + ntop_bottom + nbottom_top)

if __name__ == "__main__":
    go()