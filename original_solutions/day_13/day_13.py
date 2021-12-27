from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
import re

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=13,year=2021).splitlines()

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
    w = 0
    h = 0
    for l in lines:
        m = re.match(r"(\d+),(\d+)", l)
        if m:
            h = max(int(m.group(1)), h)
            w = max(int(m.group(2)), w)
    a = np.ndarray((w+1, h+1), dtype=int)
    a.fill(0)
    for l in lines:
        match_point = re.match(r"(\d+),(\d+)", l)
        match_fold = re.match(r"fold along ([xy])=(\d+)", l)
        if match_point:
            a[int(match_point.group(2)),int(match_point.group(1))] = 1
        elif match_fold:
            axis = match_fold.group(1)
            pos = int(match_fold.group(2))
            if axis == "x":
                b = a[:,:pos].copy()
                b |= np.fliplr(a[:,pos+1:])
            elif axis == "y":
                b = a[:pos,:].copy()
                b |= np.flipud(a[pos+1:,:])
            a = b
            return a.sum()
    return a.sum()


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    w = 0
    h = 0
    for l in lines:
        m = re.match(r"(\d+),(\d+)", l)
        if m:
            h = max(int(m.group(1)), h)
            w = max(int(m.group(2)), w)
    a = np.ndarray((w+1, h+1), dtype=int)
    a.fill(0)
    for l in lines:
        match_point = re.match(r"(\d+),(\d+)", l)
        match_fold = re.match(r"fold along ([xy])=(\d+)", l)
        if match_point:
            a[int(match_point.group(2)),int(match_point.group(1))] = 1
        elif match_fold:
            axis = match_fold.group(1)
            pos = int(match_fold.group(2))
            if axis == "x":
                b = a[:,:pos].copy()
                b |= np.fliplr(a[:,pos+1:])
            elif axis == "y":
                b = a[:pos,:].copy()
                b |= np.flipud(a[pos+1:,:])
            a = b
    np.savetxt("out.txt", a, fmt="%d")
    return 0


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)