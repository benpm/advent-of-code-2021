from types import CodeType
from aocd import submit, get_data
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

lines = get_data(day=15,year=2021).splitlines()

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
    risk = np.array([[int(x) for x in r] for r in lines])
    s = risk.shape
    # Array of lowest total risk to reach each cell
    scrs = np.ndarray(s, dtype=int)
    scrs.fill(2**16)
    scrs[0,0] = 0
    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    go = True
    while go:
        go = False
        for r in range(s[0]):
            for c in range(s[1]):
                # Set current risk to min of self and surrounding
                prev = scrs[r,c]
                scrs[r,c] = min(
                    [scrs[r+d[0],c+d[1]] + risk[r,c] for d in dirs 
                        if r+d[0] in range(s[0]) and c+d[1] in range(s[1])]
                    + [scrs[r,c]]
                )
                if scrs[r,c] != prev:
                    go = True
    return scrs[-1,-1]


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    ir = np.array([[int(x) for x in r] for r in lines])
    risk = np.ndarray((ir.shape[0]*5, ir.shape[1]*5), dtype=int)
    s = ir.shape
    for r in range(5):
        for c in range(5):
            risk[r*s[0]:(r+1)*s[0],c*s[1]:(c+1)*s[1]] = (ir + (r+c-1)) % 9 + 1
    s = risk.shape
    # Array of lowest total risk to reach each cell
    scrs = np.ndarray(s, dtype=int)
    scrs.fill(2**16)
    scrs[0,0] = 0
    dirs = ((1,0), (-1,0), (0,1), (0,-1))
    changed = 1
    while changed:
        changed = 0
        for r in range(s[0]):
            for c in range(s[1]):
                # Set current risk to min of self and surrounding
                prev = scrs[r,c]
                scrs[r,c] = min(
                    [scrs[r+d[0],c+d[1]] + risk[r,c] for d in dirs 
                        if r+d[0] in range(s[0]) and c+d[1] in range(s[1])]
                    + [scrs[r,c]]
                )
                if scrs[r,c] != prev:
                    changed += 1
        print(changed, scrs[-1,-1])
    return scrs[-1,-1]


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)