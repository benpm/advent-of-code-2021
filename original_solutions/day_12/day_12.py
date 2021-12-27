from aocd import submit, get_data
from networkx.algorithms.assortativity import neighbor_degree
import numpy as np
import scipy.signal as sp
from sys import argv
from collections import defaultdict
from networkx import *

assert len(argv) == 4, "args: [part A/B] [example? t/f] [submit? t/f]"
assert argv[1] in ['A', 'B'], "part must be A or B"
assert argv[2] in ['t', 'f'], "example must be t or f"
assert argv[3] in ['t', 'f'], "submit must be t or f"

PART = argv[1]
EXAMPLE = (argv[2] == "t")
SUBMIT = (argv[3] == "t")

lines = get_data(day=12,year=2021).splitlines()

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
    g = Graph()
    for l in lines:
        n1 = l.split("-")[0]
        n2 = l.split("-")[1]
        g.add_node(n1)
        g.add_node(n2)
        g.add_edge(n1, n2)
    
    found = set()
    uepaths = set([("start",)])
    while len(uepaths) > 0:
        # Add to unexplored paths
        newpaths = set()
        for p in uepaths:
            for nbor in g.neighbors(p[-1]):
                if nbor == p[-1]:
                    continue # Can't go back to self
                if nbor.islower() and nbor in p:
                    continue # Can't hit lowercase nodes twice
                if nbor == "start":
                    continue # Can't hit start twice
                if nbor == "end":
                    found.add(p)
                    continue
                newpaths.add(p + (nbor,))
        uepaths = newpaths
    return len(found)


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    g = Graph()
    for l in lines:
        n1 = l.split("-")[0]
        n2 = l.split("-")[1]
        g.add_node(n1)
        g.add_node(n2)
        g.add_edge(n1, n2)
    
    found = set()
    pths = set([("start",)])
    while len(pths) > 0:
        # Add to unexplored paths
        newpaths = set()
        for p in pths:
            for c in np.unique(p):
                # Look for multiple dupe lowercase letters
                if c.islower() and p.count(c) == 2:
                    for cc in np.unique(p):
                        if c != cc and cc.islower() and p.count(cc) == 2:
                            break
                    else:
                        continue
                    break
            else:
                # No duplicate double lowercase nodes, look for new paths
                for nbor in g.neighbors(p[-1]):
                    if nbor == p[-1]:
                        continue
                    if nbor.islower() and p.count(nbor) >= 2:
                        continue # Can't hit lowercase nodes more than twice
                    if nbor == "start":
                        continue # Can't hit start twice
                    if nbor == "end":
                        found.add(p)
                        continue # Found end
                    newpaths.add(p + (nbor,))
        pths = newpaths
    return len(found)


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)