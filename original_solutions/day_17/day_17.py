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

lines = get_data(day=17,year=2021).splitlines()

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
    m = re.match(r"target area: x=(\d+)\.\.(\d+), y=-(\d+)\.\.-(\d+)", lines[0])
    Tx = range(int(m.group(1)), int(m.group(2)) + 1)
    Ty = range(-int(m.group(4)), -int(m.group(3))-1, -1)
    max_y = 0
    max_vx = 0
    max_vy = 0
    for x in range(500):
        for y in range(500):
            vx = x
            vy = y
            px = 0
            py = 0
            my = 0
            while px < Tx.stop and py > Ty.stop:
                px += vx
                py += vy
                vx = max(vx-1, 0)
                vy -= 1
                my = max(my, py)
                if px in Tx and py in Ty:
                    max_y = max(max_y, my)
                    max_vx = max(max_vx, x)
                    max_vy = max(max_vy, y)
                    break
    return max_y


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    m = re.match(r"target area: x=(\d+)\.\.(\d+), y=-(\d+)\.\.-(\d+)", lines[0])
    Tx = range(int(m.group(1)), int(m.group(2)) + 1)
    Ty = range(-int(m.group(4)), -int(m.group(3))-1, -1)
    max_y = 0
    max_vx = 0
    max_vy = 0
    n = 0
    for x in range(600):
        for y in range(-200, 500):
            vx = x
            vy = y
            px = 0
            py = 0
            my = 0
            while px < Tx.stop and py > Ty.stop:
                px += vx
                py += vy
                vx = max(vx-1, 0)
                vy -= 1
                my = max(my, py)
                if px in Tx and py in Ty:
                    n += 1
                    break
    return n


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)