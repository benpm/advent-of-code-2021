from aocd import lines, submit

ans = 0

test = False

gamma = 0
eps = 0

c = []

if test:
    with open("test.txt", "r") as f:
        lines = f.readlines()

for line in [l.strip() for l in lines if l]:
    for i, sn in enumerate(line):
        if len(c) <= i:
            c.append([0,0])
        n = int(sn)
        c[i][n] += 1

for i, cs in enumerate(c):
    if cs[1] > cs[0]:
        x = 1
    else:
        x = 0
    print(x)
    gamma = (gamma | (x << (len(c) - i - 1)))
    if cs[1] < cs[0]:
        x = 1
    else:
        x = 0
    eps = (eps | (x << (len(c) - i - 1)))

ans = gamma * eps
print(gamma, eps, ans)
submit(ans)