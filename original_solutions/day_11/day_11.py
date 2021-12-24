from aocd import submit, get_data
import numpy as np
from numpy.core.fromnumeric import shape
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

lines = get_data(day=11,year=2021).splitlines()

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
    a: np.ndarray = np.array([[int(x) for x in r] for r in lines])
    H,W = a.shape
    flashes = 0
    for i in range(100):
        a += 1
        while a.max() > 9:
            for r in range(H):
                for c in range(W):
                    if a[r,c] > 9:
                        flashes += 1
                        for rr in range(max(0,r-1), min(H,r+2)):
                            for cc in range(max(0,c-1), min(W,c+2)):
                                a[rr,cc] += 1
                        a[r,c] = -9999
        a[a < 0] = 0

    return flashes


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    a: np.ndarray = np.array([[int(x) for x in r] for r in lines])
    H,W = a.shape
    flashes = 0
    step = 0
    while a.sum() > 0:
        a += 1
        while a.max() > 9:
            for r in range(H):
                for c in range(W):
                    if a[r,c] > 9:
                        flashes += 1
                        for rr in range(max(0,r-1), min(H,r+2)):
                            for cc in range(max(0,c-1), min(W,c+2)):
                                a[rr,cc] += 1
                        a[r,c] = -9999
        a[a < 0] = 0
        step += 1

    return step


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)