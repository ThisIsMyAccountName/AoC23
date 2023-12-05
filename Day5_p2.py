seeds = []
maps = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
map_idx = 0
grab_name = False
with open('inputs/day5_test.txt') as file:
    for i,x in enumerate(file):
        if i == 0:
            t = list(map(int, x.split(":")[1].split()))
            seeds = [(t[i], t[0]+t[i+1]-1) for i in range(0, len(t),2)]
            continue
        if x == "\n":
            grab_name = True
            continue
        if grab_name:
            grab_name = False
            map_idx += 1
            continue
        dest, src, amount = list(map(int, x.split()))
        maps[map_idx].append((dest, src, amount))

for val in range(79000000,80000000):
    new = val
    for map_idx in range(7,0,-1):
        for dest, src, amount in maps[map_idx]:
            if dest <= new < dest + amount:
                new = src + (new - dest)
                break
    for start, amount in seeds:
        if start <= new < start + amount:
            print(val)
            exit()
