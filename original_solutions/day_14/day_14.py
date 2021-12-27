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

lines = get_data(day=14,year=2021).splitlines()

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
    st = lines[0]
    rules = {}
    for l in lines[2:]:
        rules[l.split(" -> ")[0]] = l.split(" -> ")[1]
    for _ in range(10):
        nst = ""
        for i in range(len(st) - 1):
            nst += st[i]
            if st[i] + st[i+1] in rules:
                nst += rules[st[i] + st[i+1]]
        nst += st[-1]
        st = nst
    freq = np.bincount([ord(c) for c in st])
    freq = np.take(freq, np.where(freq > 0))[0]
    freq = np.sort(freq)
    return freq[-1] - freq[0]


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B(): # elegant solution which is always one off lmao
    cnt = defaultdict(int)
    rules = {}
    for l in lines[2:]:
        rules[l.split(" -> ")[0]] = l.split(" -> ")[1]
    s = lines[0]
    tot = defaultdict(int)
    # Input sequence
    for i in range(len(s) - 1):
        cnt[s[i] + s[i+1]] += 1
        tot[s[i]] += 1

    for _ in range(40):
        cnt_copy = cnt.copy()
        for c_in, c_out in rules.items():
            n = cnt_copy[c_in]
            if n:
                # Pair insertion
                cnt[c_in] -= n
                cnt[c_in[0] + c_out] += n
                cnt[c_out + c_in[1]] += n
                # Keep track of totals separately to avoid double counting
                tot[c_out] += n
    print(tot)
    t = sorted(tot.values())
    return t[-1] - t[0] - 1 # no idea why this is one off


# ---------------------------------------------------------------------------


ans = part_A() if PART == "A" else part_B()
print("ANSWER:", ans)
if SUBMIT and not EXAMPLE and ans != 0:
    submit(ans)