def read_input(filename):
    with open(filename) as f:
        line = f.readline().strip()
    return line

def decode_line(input_line):
    output_line = []
    next_file = 0
    next_location = 0
    while next_location < len(input_line):
        l_program = int(input_line[next_location])
        next_location += 1
        for i in range(l_program):
            output_line.append(next_file)
        next_file += 1
        try:
            l_space = int(input_line[next_location])
            for i in range(l_space):
                output_line.append(".")
            next_location += 1
        except:
            pass
    return output_line

def defrag(dline):
    while True:
        try:
            first_empty = dline.index(".")
        except ValueError:
            break
        moving_block = dline[-1]
        dline[first_empty] = moving_block
        dline = dline[:-1]
    return dline

def calculate_checksum(ddline):
    csum = 0
    for p,v in enumerate(ddline):
        csum += p*v
    return csum

def go():
    input = read_input("input.txt")
    dline = decode_line(input)
    ddline = defrag(dline)
    cksum = calculate_checksum(ddline)
    print(cksum)

if __name__ == "__main__":
    go()