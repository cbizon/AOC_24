def read_input(infile):
    with open(infile) as f:
        towels = [ z.strip() for z in f.readline().strip().split(',')]
        blank = f.readline()
        patterns = []
        for line in f:
            patterns.append( line.strip() )
    return towels, patterns

def is_possible(pattern,towels):
    #yeah yeah recursion whatever
    partials = ['']
    while len(partials) > 0:
        partial = partials.pop()
        left = pattern[ len(partial): ]
        for towel in towels:
            if left.startswith(towel):
                new_partial = partial + towel
                if new_partial == pattern:
                    return True
                partials.append(new_partial)
    return False

def go():
    towels, patterns = read_input("input.txt")
    n_possible = 0
    for pattern in patterns:
        if is_possible(pattern,towels):
            n_possible += 1
    print(n_possible)

if __name__ == "__main__":
    go()