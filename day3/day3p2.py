import re

def read_input():
    with open("input.txt") as f:
        return f.read()

def eval(s):
    x = s.split(",")
    return int(x[0][4:]) * int(x[1][:-1])

def go():
    input = read_input()
    x = re.findall("(mul\\([0-9]{1,3},[0-9]{1,3}\\)|do\\(\\)|don't\\(\\))", input)
    total = 0
    active = True
    for i in x:
        if i == "do()":
            active = True
        elif i == "don't()":
            active = False
        elif active:
            total += eval(i)
    print(total)

if __name__ == "__main__":
    go()