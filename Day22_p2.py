from collections import defaultdict
bricks = sorted([[[int(y) for y in k.split(",")] for k in x.split("~")] for x in open('inputs/day22.txt').read().splitlines()], key=lambda x: x[0][2])

def drop(bricks):
    tower = defaultdict(int)
    for brick in bricks:
        (x0, y0, z0), (x1, y1, z1) = brick
        cords = []
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                cords.append((x, y))
        height = 1
        for xy in cords:
            height = max(height, tower[xy] + 1)
        fall = z0 - height
        brick[0][2] -= fall
        brick[1][2] -= fall
        for xy in cords:
            tower[xy] = z1 - fall

def solve(bricks, skip):
    down = 0
    tower = defaultdict(int)
    for brick in bricks:
        if brick == skip:
            continue
        (x0, y0, z0), (x1, y1, z1) = brick
        cords = []
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                cords.append((x, y))
        height = 1
        for xy in cords:
            height = max(height, tower[xy] + 1)
        fall = z0 - height
        down += 1 if fall else 0
        for xy in cords:
            tower[xy] = z1 - fall
    return down

drop(bricks)
print(sum(solve(bricks, brick) for brick in bricks))