import copy

# 4558 low

map = [[s for s in l] for l in open('./input.txt').read().split('\n')]

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '^':
            px = x
            py = y
print(px,py)
sx = px
sy = py

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
dir = 0
seen = set()
seen.add((px,py))

while True:
        dx,dy = dirs[dir]
        nx = px + dx
        ny = py + dy
        if not 0 <= nx < len(map[0]) or not 0 <= ny < len(map):
            break
        
        if map[ny][nx] == '#':
            dir = (dir+1) % 4
            continue
        
        px = nx
        py = ny
        seen.add((px,py))

def check_loop(px,py,dir,n_map):
    loop_set = set()
    while True:
        if (dir,(px,py)) in loop_set:
            return True
        loop_set.add((dir,(px,py)))

        dx,dy = dirs[dir]
        nx = px + dx
        ny = py + dy
        if not 0 <= nx < len(n_map[0]) or not 0 <= ny < len(n_map):
            return False
        
        if n_map[ny][nx] == '#':
            dir = (dir+1) % 4
            continue
        
        px = nx
        py = ny
        # seen.add((px,py))

res = set()
for x,y in seen:
    if x == sx and y == sy:
        continue
    new_map = copy.deepcopy(map)
    new_map[y][x] = '#'
    if check_loop(sx,sy,0,new_map):
        res.add((x,y))
print(len(res))
