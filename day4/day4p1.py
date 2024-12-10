import numpy

def read_input(infname):
    puzzle_input = []
    with open(infname) as f:
        for line in f:
            puzzle_input.append([x for x in line.strip()])
    return puzzle_input

def count_per_line(line):
    s = ''.join(line)
    return s.count("XMAS")

def count_all(lines):
    total = 0
    for line in lines:
        total += count_per_line(line)
    return total

def invert(lines):
    newlines = []
    for line in lines:
        newlines.append(line[::-1])
    return newlines

def transpose(lines):
    return numpy.transpose(lines)

def diags(lines):
    new_array = []
    mindiag = -len(lines) + 1
    maxdiag = len(lines[0]) - 1
    for i in range(mindiag, maxdiag):
        new_array.append(numpy.diagonal(lines, i))
    return new_array

def go():
    puzzle_input = read_input("input.txt")
    nleft_right = count_all(puzzle_input)
    new_input = invert(puzzle_input)
    nright_left = count_all(new_input)
    tpose = transpose(puzzle_input)
    ntop_bottom = count_all(tpose)
    new_input = invert(tpose)
    nbottom_top = count_all(new_input)
    d1 = diags(puzzle_input)
    ntopleft_bottomright = count_all(d1)
    id1 = invert(d1)
    nbottomright_topleft = count_all(id1)
    d2 = diags(invert(puzzle_input))
    ntopright_bottomleft = count_all(d2)
    id2 = invert(d2)
    nbottomleft_topright = count_all(id2)
    print(nleft_right, nright_left, ntop_bottom, nbottom_top,
            ntopleft_bottomright, nbottomright_topleft, ntopright_bottomleft, nbottomleft_topright)
    print(nleft_right + nright_left + ntop_bottom + nbottom_top +
            ntopleft_bottomright + nbottomright_topleft + ntopright_bottomleft + nbottomleft_topright)


if __name__ == "__main__":
    go()