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

lines = [l.strip() for l in lines]
if lines[-1] == "":
    lines = lines[:-1]

# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------


def part_A():
    fs = [int(f) for f in lines[0].split(",")]
    for i in range(80):
        toi = len(fs)
        for i in range(toi):
            fs[i] = (fs[i] - 1)
            if fs[i] < 0:
                fs[i] = 6
                fs.append(8)
    print(len(fs))
    return len(fs)


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    fs = defaultdict(int)
    for n in lines[0].split(","):
        fs[(int(n) - 1) % 7] += 1
    fish = len(lines[0].split(","))
    sfs = defaultdict(int)
    for i in range(255):
        sfsc = sfs.copy()
        for n, occ in fs.items():
            if occ > 0 and (i) % 7 == n:
                fish += occ
                sfs[(i) % 9] += occ
        for n, occ in sfsc.items():
            if occ > 0 and (i) % 9 == n:
                fish += occ
                fs[(i) % 7] += occ

    return fish



# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)