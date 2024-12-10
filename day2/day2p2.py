def report_is_safe(report):
    diffs = [report[i + 1] - report[i] for i in range(len(report) - 1)]
    mindiffs = min(diffs)
    maxdiffs = max(diffs)
    # isn't monotonic
    if mindiffs * maxdiffs <= 0:
        return False
    # too big down
    elif mindiffs < -3:
        return False
    # too big up
    elif maxdiffs > 3:
        return False
    else:
        return True

def test_safety(report):
    if report_is_safe(report):
        return True
    for i in range(len(report)):
        newreport = report[:i] + report[i+1:]
        if len(newreport) != len(report) - 1:
            print("Error")
        if report_is_safe(newreport):
            return True
    print(report)
    return False

def go():
    nsafe = 0
    n = 0
    with open("input.txt") as f:
        for line in f:
            n += 1
            x = line.strip().split()
            report = [int(i) for i in x]
            if test_safety(report):
                nsafe += 1
    print(f"{nsafe} out of {n} are safe")

if __name__ == "__main__":
    go()