from aocd import lines, submit, get_data
import numpy as np
from numpy.ma import masked_array

PART = 1
EXAMPLE = False

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()

lines = [l.strip() for l in lines]

# ---------------------------------------------------------------------------
# Part A
# ---------------------------------------------------------------------------

def part_A():
    b: list[np.ndarray] = []
    last = np.ndarray((5, 5), dtype=int)
    d = np.array([int(x) for x in lines[0].split(",") if x], dtype=int)
    i = 0
    for l in lines[2:]:
        if len(l) == 0:
            b.append(last)
            last = last.copy()
            i = 0
            continue
        last[i] = [int(x) for x in l.split(" ") if x]
        i += 1
    b.append(last)
    for cal in d:
        print(cal)
        for bb in b:
            if cal in bb:
                x = np.where(bb == cal)
                bb[x] = 0
                for r in bb:
                    if np.sum(r) == 0:
                        print(bb)
                        return np.sum(bb) * cal
                for c in np.rot90(bb):
                    if np.sum(c) == 0:
                        print(bb)
                        return np.sum(bb) * cal
                # if np.trace(bb) == 0:
                #     print(bb)
                #     return 0
                # if np.trace(np.rot90(bb)) == 0:
                #     print(bb)
                #     return 0
    return 0


# ---------------------------------------------------------------------------
# Part B
# ---------------------------------------------------------------------------


def part_B():
    b: list[np.ndarray] = []
    last = np.ndarray((5, 5), dtype=int)
    d = np.array([int(x) for x in lines[0].split(",") if x], dtype=int)
    i = 0
    for l in lines[2:]:
        if len(l) == 0:
            b.append(last)
            last = last.copy()
            i = 0
            continue
        last[i] = [int(x) for x in l.split(" ") if x]
        i += 1
    b.append(last)
    won = []
    for cal in d:
        print(cal)
        for I,bb in enumerate(b):
            if I in won:
                continue
            if cal in bb:
                x = np.where(bb == cal)
                bb[x] = 0
                for r in bb:
                    if np.sum(r) == 0:
                        won.append(I)
                        break
                else:
                    for c in np.rot90(bb):
                        if np.sum(c) == 0:
                            won.append(I)
                            break
        if len(won) == len(b):
            I = won[-1]
            print(b[I])
            print(np.sum(b[I]), cal)
            return np.sum(b[I]) * cal
    return 0


# ---------------------------------------------------------------------------


ans = part_A() if PART == 0 else part_B()
print("ANSWER:", ans)
if not EXAMPLE and ans != 0:
    submit(ans)