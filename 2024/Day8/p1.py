# 387 - low

map = [[s for s in l] for l in open('./input.txt').read().split('\n')]
locations = {}
for y in range(len(map)):
    for x in range(len(map[0])):
        char = map[y][x]
        if char != '.':
            if char in locations:
                locations[char].append((x,y))
            else:
                locations[char] = [(x,y)]

for k,v in locations.items():
    print(k,v)

anti_nodes = set()
for _,locs in locations.items():
    for i in range(len(locs)):
        for j in range(i+1,len(locs)):
            x1,y1 = locs[i]
            x2,y2 = locs[j]

            anti1x = x2 + (x2-x1)
            anti1y = y2 + (y2-y1)
            if 0 <= anti1x < len(map[0]) and 0 <= anti1y < len(map):
                anti_nodes.add((anti1x,anti1y))

            anti2x = x1 + (x1-x2)
            anti2y = y1 + (y1-y2)
            if 0 <= anti2x < len(map[0]) and 0 <= anti2y < len(map):
                anti_nodes.add((anti2x,anti2y))

print(len(anti_nodes))