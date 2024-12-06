# 4558 low

map = [[s for s in l] for l in open('./input.txt').read().split('\n')]

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '^':
            px = x
            py = y
print(px,py)
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
print(len(seen))

