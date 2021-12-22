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

lines = get_data(day=10,year=2021).splitlines()

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

lc = ["[", "{", "<", "("]
mp = {c:i for i,c in enumerate(lc)}
rc = ["]", "}", ">", ")"]
mp.update({c:i for i,c in enumerate(rc)})
pts = {")":3, "]":57, "}":1197, ">":25137}

def part_A():
    ans = 0
    for l in lines:
        st = []
        for c in l:
            if c in lc:
                st.append(c)
            else:
                if mp[c] == mp[st[-1]]:
                    st.pop()
                else:
                    ans += pts[c]
                    break
    return ans


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    scrs = []
    pts = {"(":1, "[":2, "{":3, "<":4}
    for l in lines:
        st = []
        scr = 0
        for c in l:
            if c in lc:
                st.append(c)
            else:
                if mp[c] == mp[st[-1]]:
                    st.pop()
                else:
                    break
        else:
            # Complete line
            for c in reversed(st):
                scr = (scr * 5) + pts[c]
            scrs.append(scr)
    scrs = np.array(scrs)
    return np.median(scrs)


# ---------------------------------------------------------------------------


ans = int(part_A() if PART == "A" else part_B())
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)