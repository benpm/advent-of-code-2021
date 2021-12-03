from aocd import lines, submit

PART = 0
EXAMPLE = True

if EXAMPLE:
    with open("test.txt", "r") as f:
        lines = f.readlines()

lines = [l.strip() for l in lines if l != "\n"]


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
if not EXAMPLE and ans != 0:
    submit(ans)