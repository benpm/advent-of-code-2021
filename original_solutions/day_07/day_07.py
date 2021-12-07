from aocd import lines, submit
import numpy as np
from sys import argv
from collections import defaultdict

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

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
    cbs = np.array([int(n) for n in lines[0].split(",")])
    st = cbs.min()
    ed = cbs.max()
    mn = 2**32
    for i in range(st, ed+1):
        dst = np.abs(cbs - i)
        if dst.sum() < mn:
            mn = dst.sum()
    ans = mn
    return ans


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    cbs = np.array([int(n) for n in lines[0].split(",")])
    st = cbs.min()
    ed = cbs.max()
    mn = 2**32
    for i in range(st, ed+1):
        dst = (np.abs(cbs - i) * (np.abs(cbs - i) + 1)) // 2
        if dst.sum() < mn:
            mn = dst.sum()
    ans = mn
    return ans


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)