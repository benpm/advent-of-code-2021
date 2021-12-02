from aocd import lines, submit

lastn = -1
inc = 0
dec=0
for line in [l.strip() for l in lines if l]:
    if lastn == -1:
        lastn = int(line)
    n = int(line)
    if n > lastn:
        inc += 1
    if n < lastn:
        dec += 1
    lastn = n

print(inc)
