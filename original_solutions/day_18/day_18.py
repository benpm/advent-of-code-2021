from aocd import submit, get_data
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
from itertools import permutations, product, repeat

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=18,year=2021).splitlines()

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

def tostr(fsh):
    rep = ""
    for i,c in enumerate(fsh[:-1]):
        if isinstance(c, int):
            if fsh[i-1] == "]":
                rep += ","
            rep += str(c)
            if type(fsh[i+1]) == int or fsh[i+1] == "[":
                rep += ","
        else:
            rep += c
            if c == "]" and fsh[i+1] == "[":
                rep += ","
    rep += fsh[-1]
    return rep

def fsh_reduce(fsh):
    reduced = False
    while not reduced:
        reduced = True
        d = -1
        for i,c in enumerate(fsh):
            if c == "[": d += 1
            elif c == "]": d -= 1
            elif d >= 4 and type(fsh[i+1]) == int:
                # explode
                a = fsh[i]
                b = fsh[i+1]
                for _ in range(4): fsh.pop(i-1)
                fsh.insert(i-1, 0)
                for ii in range(i-2, 0, -1):
                    if isinstance(fsh[ii], int):
                        fsh[ii] += a
                        break
                for ii in range(i, len(fsh)):
                    if isinstance(fsh[ii], int):
                        fsh[ii] += b
                        break
                reduced = False
                break
        if not reduced: continue
        d = -1
        for i,c in enumerate(fsh):
            if c == "[": d += 1
            elif c == "]": d -= 1
            elif c >= 10:
                # split
                fsh.pop(i)
                fsh.insert(i, "]")
                fsh.insert(i, c - c//2)
                fsh.insert(i, c//2)
                fsh.insert(i, "[")
                reduced = False
                break

def fsh_mag(fsh):
    # compute magnitude
    fsh = fsh.copy()
    while len(fsh) > 1:
        for i in range(len(fsh)):
            if type(fsh[i]) == int and type(fsh[i+1]) == int:
                s = fsh[i]*3 + fsh[i+1]*2
                for _ in range(4): fsh.pop(i-1)
                fsh.insert(i-1, s)
                break
    return fsh[0]

def part_A():
    fsh = None
    for l in lines:
        nfsh = [(int(c) if c.isdigit() else c) for c in l if c != ","]
        if fsh is None:
            fsh = nfsh
        else:
            fsh = ["[", *fsh, *nfsh, "]"]
        fsh_reduce(fsh)
    return fsh_mag(fsh)

# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    fsh_list = []
    for l in lines:
        fsh_list.append([(int(c) if c.isdigit() else c) for c in l if c != ","])
    best = 0
    for a,b in product(fsh_list, repeat=2):
        fsh = ["[", *a, *b, "]"]
        fsh_reduce(fsh)
        best = max(best, fsh_mag(fsh))
    return best


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)