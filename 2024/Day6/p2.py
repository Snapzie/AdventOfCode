# 1757 high
# 1559 low
# 1658 high
import copy
map = [[s for s in l] for l in open('./input.txt').read().split('\n')]

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '^':
            px = x
            py = y
print(px,py)

def check_loop(lpx,lpy,ldir,lmap):
    loop_set = set()
    ldx,ldy = dirs[ldir]
    ox = lpx + ldx
    oy = lpy + ldy
    if ox == sx and oy == sy:
        return None
    if not 0 <= ox < len(lmap[0]) or not 0 <= oy < len(lmap):
        return None
    if lmap[oy][ox] == '#':
        return None
    lmap[oy][ox] = '#'
    while True:
        if ((ldir,(lpx,lpy)) in loop_set):
            return (ox,oy)
        loop_set.add((ldir,(lpx,lpy)))

        ldx,ldy = dirs[ldir]
        lnx = lpx + ldx
        lny = lpy + ldy
        if not 0 <= lnx < len(lmap[0]) or not 0 <= lny < len(lmap):
            return None
        
        if lmap[lny][lnx] == '#':
            ldir = (ldir+1) % 4
            continue
        
        lpx = lnx
        lpy = lny
        


dirs = [(0,-1),(1,0),(0,1),(-1,0)]
dir = 0
sx = px
sy = py
seen = set()
while True:
    map_copy = copy.deepcopy(map)
    pos = check_loop(px,py,dir,map_copy)
    if pos:
        x = pos[0]
        y = pos[1]
        seen.add((x,y))
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
print(len(seen))

