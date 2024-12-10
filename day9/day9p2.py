def read_input(filename):
    with open(filename) as f:
        line = f.readline().strip()
    return line

class FileBlock:
    def __init__(self, filenum, location, length):
        self.filenum = filenum
        self.location = location
        self.length = length

class EmptyBlock:
    def __init__(self, location, length):
        self.location = location
        self.length = length

def decode_line(input_line):
    files = []
    empties = []
    next_file = 0
    next_block = 0
    next_location = 0
    while next_block < len(input_line):
        l_block = int(input_line[next_block])
        if next_block % 2 == 0:
            fileblock = FileBlock(next_file, next_location, l_block)
            files.append(fileblock)
            next_file += 1
        else:
            emptyblock = EmptyBlock(next_location, l_block)
            empties.append(emptyblock)
        next_block += 1
        next_location += l_block
    return files,empties

def find_empty(empties, max_location, length):
    #the empties are sorted by location
    for empty in empties:
        if empty.location > max_location:
            return None
        if empty.length >= length:
            return empty
    return None

def move(fileblock,empty):
    print( f"Moving {fileblock.filenum} from {fileblock.location} to {empty.location}" )
    fileblock.location = empty.location
    empty.location = empty.location + fileblock.length
    empty.length = empty.length - fileblock.length
    # if the empty is now zero, remove it
    return empty.length == 0

def defrag(files, empties):
    # This is the brute force approach, you could do some playing with sorting the empties to make things quicker
    for fileblock in files[::-1]:
        empty = find_empty(empties, fileblock.location, fileblock.length)
        if empty is not None:
            delete_empty = move(fileblock, empty)
            if delete_empty:
                empties.remove(empty)

def calculate_checksum(files):
    csum = 0
    for fileblock in files:
        for i in range(fileblock.length):
            loc = i + fileblock.location
            csum += loc * fileblock.filenum
    return csum

def go():
    input = read_input("input.txt")
    files, empties = decode_line(input)
    files.sort(key = lambda x: x.location)
    defrag(files, empties)
    cksum = calculate_checksum(files)
    print(cksum)
    files.sort(key = lambda x: x.location)

if __name__ == "__main__":
    go()