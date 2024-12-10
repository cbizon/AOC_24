import re

def read_input():
    with open("input.txt") as f:
        return f.read()

def eval(s):
    x = s.split(",")
    return int(x[0][4:]) * int(x[1][:-1])

def go():
    input = read_input()
    x = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", input)
    total = 0
    for i in x:
        total += eval(i)
    print(total)

if __name__ == "__main__":
    go()