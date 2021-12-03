from aocd import lines, submit

ans = 0

example = True

if example:
    with open("test.txt", "r") as f:
        lines = f.readlines()

for line in [l.strip() for l in lines if l]:
    print(line)

#submit(ans)