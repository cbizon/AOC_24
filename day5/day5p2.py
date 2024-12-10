from collections import defaultdict
from functools import partial,cmp_to_key

def read_input(infile):
    rules=[]
    updates=[]
    with open(infile) as f:
        line=f.readline()
        while line != "\n":
            rules.append(line.strip())
            line=f.readline()
        for line in f:
            updates.append(line.strip().split(','))
    return rules, updates

def parse_rules(rules):
    a_before_b = defaultdict(set)
    follows = defaultdict(set)
    for rule in rules:
        x = rule.split("|")
        a_before_b[x[0]].add(x[1])
    return a_before_b

def check(update, precedes):
    for pagenum,page1 in enumerate(update):
        for page2 in update[pagenum+1:]:
            if page1 in precedes[page2]:
                return False
    return True

def score(update):
    n = (len(update)+1)/2 - 1
    return int(update[int(n)])

def compare(a,b,a_before_b):
    if a in a_before_b[b]:
        return 1
    if b in a_before_b[a]:
        return -1
    return 0


def fix(update, a_before_b):
    new_update = sorted(update,key = cmp_to_key(partial(compare,a_before_b=a_before_b)))
    return new_update

def go():
    rules, updates = read_input("input.txt")
    precedes = parse_rules(rules)
    total = 0
    for update in updates:
        correct = check(update,precedes)
        #if correct:
        #    total += score(update)
        if not correct:
            fixed = fix(update, precedes)
            total += score(fixed)
    print(total)

if __name__ == "__main__":
    go()
