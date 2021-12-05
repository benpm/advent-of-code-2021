from aocd import lines, submit
import numpy as np

PART = 0
EXAMPLE = True
SUBMIT = False

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()

lines = [l.strip() for l in lines]
if lines[-1] == "":
    lines = lines[:-1]


# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------


def part_A():
    for l in lines:
        print(l)
    return 0


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    for l in lines:
        print(l)
    return 0


# ---------------------------------------------------------------------------


ans = part_A() if PART == 0 else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)