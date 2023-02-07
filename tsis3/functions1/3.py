def solve(numheads, numlegs):
    for chickens in range(heads + 1):
        rabbits = heads - chickens
        if 2*chickens + 4*rabbits == legs:
            return (chickens, rabbits)
    return (None, None)


numheads = input()
numheads = int(numheads)
numlegs = input()
numlegs = int(numlegs)
print(solve(numheads, numlegs))