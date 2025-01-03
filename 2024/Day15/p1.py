map, instructions = open('input.txt').read().split('\n\n')
map = [[c for c in l] for l in map.split('\n')]
instructions = instructions.replace('\n','')

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '@':
            px = x
            py = y
            map[y][x] = '.'

def box_movable(bx,by,dx,dy):
    if map[by+dy][bx+dx] == '#':
        return False
    elif map[by+dy][bx+dx] == '.':
        map[by+dy][bx+dx] = 'O'
        return True
    else:
        return box_movable(bx+dx,by+dy,dx,dy)

dirs = {'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}
for inst in instructions:
    dx,dy = dirs[inst]
    nx = px + dx
    ny = py + dy

    if map[ny][nx] == '.':
        px = nx
        py = ny
    elif map[ny][nx] == 'O':
        if box_movable(nx,ny,dx,dy):
            map[ny][nx] = '.'
            px = nx
            py = ny

res = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 'O':
            res += y*100 + x
print(res)