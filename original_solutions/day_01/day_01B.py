from aocd import lines, submit

lastn = -1
inc = 0
dec = 0
last3 = 0
i = 0
nums = [int(l) for l in lines if l]
for i, n in enumerate(nums):
    if i < 2:
        continue
    else:
        sm = sum(nums[i - 2:i + 1])
        if i == 2:
            lastn = sm
        if sm < lastn:
            dec += 1
        elif sm > lastn:
            inc += 1
        lastn = sm

submit(inc)
