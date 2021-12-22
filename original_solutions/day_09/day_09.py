from aocd import lines, submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=9,year=2021).splitlines()

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
    a: np.ndarray = np.array([[int(x) for x in l] for l in lines]) 
    s = a.shape
    rl = np.ndarray(s, dtype=int)
    for x in range(s[0]):
        for y in range(s[1]):
            for xx, yy in (-1,0), (1,0), (0,-1), (0,1):
                if x + xx >= 0 and x + xx < s[0] and y + yy >= 0 and y + yy < s[1]:
                    if a[x+xx, y+yy] <= a[x, y]:
                        rl[x, y] = 0
                        break
            else:
                rl[x, y] = a[x, y] + 1

    return rl.sum()


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------

def cpf(x, y):
    return ((x + y) * (x + y + 1)) // 2 + y

def part_B():
    a: np.ndarray = np.array([[int(x) for x in l] for l in lines]) 
    s = a.shape
    # Build map of basin indices
    bmap = np.ndarray(s, dtype=int)
    bmap.fill(-1)
    for x in range(s[0]):
        for y in range(s[1]):
            if a[x,y] == 9: continue
            ix = x
            iy = y
            st = []
            # Loop to find basin for current location
            while True:
                if bmap[ix, iy] != -1:
                    idx = bmap[ix, iy]
                    break
                st.append((ix, iy))
                for xx, yy in (-1,0), (1,0), (0,-1), (0,1):
                    nx = ix + xx
                    ny = iy + yy
                    if nx in range(s[0]) and ny in range(s[1]) \
                        and a[nx, ny] < a[ix, iy]:
                        ix = nx
                        iy = ny
                        break
                else:
                    idx = cpf(ix, iy)
                    break

            bmap[ix, iy] = idx
            for ix, iy in st:
                bmap[ix, iy] = idx
    

    # Determine basin sizes
    idxs = np.unique(bmap)
    bsz = []
    for idx in idxs:
        if idx != -1:
            bsz.append(np.sum(bmap == idx))
    bsz.sort()

    return bsz[-3] * bsz[-2] * bsz[-1]


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)