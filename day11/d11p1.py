def read_input(infile):
    input = []
    with open(infile) as f:
        for line in f:
            input.append( line.strip().split() )
    return input

def go():
    input = read_input("input.txt")
    print(input)

if __name__ == "__main__":
    go()