from time import sleep
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

nums = {
    0: (0,1,2,4,5,6),
    1: (2,5),
    2: (0,2,3,4,6),
    3: (0,2,3,5,6),
    4: (1,2,3,5),
    5: (0,1,3,5,6),
    6: (0,1,3,4,5,6),
    7: (0,2,5),
    8: (0,1,2,3,4,5,6),
    9: (0,1,2,3,5,6),
}

rnums = {v:k for k,v in nums.items()}

lets = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6
}
rlets = {v:k for k,v in lets.items()}

def part_A():
    counts = defaultdict(int)
    for l in lines:
        outs = l.split(" | ")[1].split(" ")
        for d in outs:
            inum = -1
            if len(d) == 2: inum = 1
            elif len(d) == 3: inum = 7
            elif len(d) == 4: inum = 4
            elif len(d) == 5:
                continue
            elif len(d) == 6:
                continue
            elif len(d) == 7: inum = 8
            
            if inum != -1:
                counts[inum] += 1
    return counts[1] + counts[4] + counts[7] + counts[8]


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    counts = defaultdict(int)
    for l in lines:
        digs = l.split(" | ")[0].split(" ")
        outs = l.split(" | ")[1].split(" ")
        aldigs = digs + outs
        psegmap = {rlets[x]: set(range(7)) for x in range(7)}
        while sum(len(x) for x in psegmap.values()) > 7:
            print(psegmap)
            sleep(.25)
            for digit in aldigs:
                inum = -1
                x = None
                if len(digit) == 2: inum = 1
                elif len(digit) == 3: inum = 7
                elif len(digit) == 4: inum = 4
                elif len(digit) == 5:
                    x = set([2,3,5])
                    continue
                elif len(digit) == 6:
                    x = set([0,6,9])
                    continue
                elif len(digit) == 7:
                    inum = 8
                
                if x != None:
                    continue
                
                if inum == -1:
                    continue
                
                cantmapto = set([lets[i] for i in set(lets.keys()).difference(list(digit))])
                for i,d in enumerate(digit):
                    psegmap[d].difference_update(cantmapto)
            
            # remove all possible out segments that exist in duped binary sets
            csegmap = psegmap.copy()
            for inseg, outsegs in csegmap.items():
                if len(outsegs) == 2:
                    for xinseg, xoutsegs in csegmap.items():
                        if outsegs == xoutsegs:
                            for x, y in psegmap.items():
                                if xinseg != x:
                                    y.difference_update(xoutsegs)
                            break
                    else:
                        break
        for outn in outs:
            dig = set()
            for d in outn:
                dig.add(segmap[d])
            counts[rnums[tuple(dig)]] += 1
    print(counts)
    return 0


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)