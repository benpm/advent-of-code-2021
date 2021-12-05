from aocd import lines, submit, data
import numpy as np
import sys

np.set_printoptions(threshold=sys.maxsize)

PART = 1
EXAMPLE = False
SUBMIT = False

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()
    data = "\n".join(lines)

lines = [l.strip() for l in lines]
if lines[-1] == "":
    lines = lines[:-1]

# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------


def part_A():
    s = np.ndarray((1000,1000), dtype=np.int)
    s.fill(0)
    for l in lines:
        p = l.split(" -> ")
        x1, y1 = [int(x) for x in p[0].split(",")]
        x2, y2 = [int(x) for x in p[1].split(",")]
        if x1 == x2 or y1 == y2:
            dx = np.sign(x2 - x1)
            dy = np.sign(y2 - y1)
            if dx == 0:
                for y in range(y1, y2 + dy, dy):
                    s[x1,y] += 1
            elif dy == 0:
                for x in range(x1, x2 + dx, dx):
                    s[x,y1] += 1
    return (s >= 2).sum()


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    s = np.ndarray((1000,1000), dtype=np.int)
    s.fill(0)
    for l in lines:
        p = l.split(" -> ")
        x1, y1 = [int(x) for x in p[0].split(",")]
        x2, y2 = [int(x) for x in p[1].split(",")]
        dx = np.sign(x2 - x1)
        dy = np.sign(y2 - y1)
        if dx == 0:
            y = y1
            while np.sign(y2 - y) == dy or (y2 == y):
                s[x1,(y)] += 1
                y += dy
        elif dy == 0:
            x = x1
            while np.sign(x2 - x) == dx or (x2 == x):
                s[(x),y1] += 1
                x += dx
        else:
            x = x1
            y = y1
            while np.sign(y2 - y) == dy or (y2 == y):
                while np.sign(x2 - x) == dx or (x2 == x):
                    s[(x),y] += 1
                    x += dx
                    y += dy
    return (len(np.where(s >= 2)[0]))


# ---------------------------------------------------------------------------


ans = part_A() if PART == 0 else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)