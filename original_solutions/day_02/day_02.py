from aocd import lines, submit

h = 0
d = 0
aim = 0

for line in [l.strip() for l in lines if l]:
    w = line.split(" ")[0]
    n = int(line.split(" ")[1])

    if w == "forward":
        h += n
        d += aim * n
    elif w == "down":
        aim += n
    elif w == "up":
        aim -= n

print(h * d)