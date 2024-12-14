def go():
    # we get a vertical convergence on 7 + 101 x, for integral x
    # we get a horizontal converence on 53 + 103 y for integral y
    verts = set( [ 7 + 101 * x for x in range(1000) ])
    horz = set( [53 + 103 * y for y in range (1000)])
    both = verts.intersection(horz)
    print(both)
    print(min(both))

if __name__ == "__main__":
    go()