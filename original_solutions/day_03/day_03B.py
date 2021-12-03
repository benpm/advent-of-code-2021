from aocd import lines, submit
from copy import deepcopy

ans = 0

test = False

gamma = 0
eps = 0


if test:
    with open("test.txt", "r") as f:
        lines = [l.strip() for l in f.readlines() if l != "\n"]

def fc(i, ls):
    c = [0, 0]
    for line in [l.strip() for l in ls if l]:
        c[int(line[i])] += 1
    return c

llox = deepcopy(lines)
i = 0
while len(llox) > 1:
    c = fc(i, llox)

    if c[0] > c[1]:
        k = 0
    elif c[0] <= c[1]:
        k = 1

    lnxt = []
    for l in llox:
        if int(l[i]) == k:
            lnxt.append(l)
        
    llox = deepcopy(lnxt)
    i += 1

print(llox)



llsc = deepcopy(lines)
i = 0
while len(llsc) > 1:
    c = fc(i, llsc)

    if c[0] > c[1]:
        k = 1
    elif c[0] <= c[1]:
        k = 0

    lnxt = []
    for l in llsc:
        if int(l[i]) == k:
            lnxt.append(l)
        
    llsc = deepcopy(lnxt)
    i += 1

print(llsc)

ans = int(llox[0], 2) * int(llsc[0], 2)
print(int(llox[0], 2) * int(llsc[0], 2))

submit(ans)