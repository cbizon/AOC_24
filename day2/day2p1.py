nsafe = 0
n = 0
with open("input.txt") as f:
    for line in f:
        n += 1
        x = line.strip().split()
        report = [int(i) for i in x]
        diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
        print(report)
        print(diffs)
        mindiffs = min(diffs)
        maxdiffs = max(diffs)
        # isn't monotonic
        if mindiffs * maxdiffs <= 0:
            print("Unsafe")
        # too big down
        elif mindiffs < -3:
            print("Unsafe")
        # too big up
        elif maxdiffs > 3:
            print("Unsafe")
        else:
            nsafe += 1
            print("Safe")

print(f"{nsafe} out of {n} are safe")