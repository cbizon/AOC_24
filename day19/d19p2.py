from collections import defaultdict

def read_input(infile):
    with open(infile) as f:
        towels = [ z.strip() for z in f.readline().strip().split(',')]
        blank = f.readline()
        patterns = []
        for line in f:
            patterns.append( line.strip() )
    return towels, patterns

def recursively_count(histories, pattern, counts):
    #Interestingly, even doing this can be slow.  So we need to avoid redoing work with the counts dict
    # where we stash partially computed results.
    n = 0
    for sub_pattern in histories[pattern]:
        if sub_pattern in counts:
            n += counts[sub_pattern]
        else:
            if len(sub_pattern) == 0:
                c = 1
            else:
                c = recursively_count(histories,sub_pattern,counts)
            counts[sub_pattern] = c
            n += c
    return n

def count_possible(pattern,towels):
    # This holds how you get to this thing
    #This is the set of things that could still lead to a result
    partials = set([''])
    # This is the complete list of how we got to a particular partial
    histories = defaultdict( set )
    histories[''] = {}
    while len(partials) > 0:
        partial = partials.pop()
        left = pattern[ len(partial): ]
        for towel in towels:
            if left.startswith(towel):
                new_partial = partial + towel
                histories[new_partial].add(partial)
                if new_partial != pattern:
                    partials.add(new_partial)
    # Now we have to add up the ways that we got there:
    counts = defaultdict(int)
    np = recursively_count(histories, pattern, counts)
    return np


def go():
    towels, patterns = read_input("input.txt")
    n_possible = 0
    for pattern in patterns:
        n_possible += count_possible(pattern,towels)
    print(n_possible)

if __name__ == "__main__":
    go()