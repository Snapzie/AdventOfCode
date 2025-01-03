map, instructions = open('input.txt').read().split('\n\n')
small_map = [[c for c in l] for l in map.split('\n')]
instructions = instructions.replace('\n','')

map = []
for y in range(len(small_map)):
    map.append([])
    for x in range(len(small_map[0])):
        if small_map[y][x] == '#':
            map[y].append('#')
            map[y].append('#')
        elif small_map[y][x] == 'O':
            map[y].append('[')
            map[y].append(']')
        elif small_map[y][x] == '.':
            map[y].append('.')
            map[y].append('.')
        elif small_map[y][x] == '@':
            map[y].append('@')
            map[y].append('.')

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '@':
            px = x
            py = y
            map[y][x] = '.'

def move_horizontal(bx,by,dx,dy):
    if map[by+dy][bx+dx] == '#':
        return False
    elif map[by+dy][bx+dx] == '.':
        map[by+dy][bx+dx] = map[by][bx]
        return True
    else:
        if move_horizontal(bx+dx,by+dy,dx,dy):
            map[by+dy][bx+dx] = map[by][bx]
            return True
        else:
            return False

def check_vertical(bx,by,dx,dy,check):
    if map[by+dy][bx+dx] == '#':
        return False
    elif check:
        if map[by+dy][bx+dx] == '.':
            if map[by][bx] == '[':
                return True and check_vertical(bx+1,by,dx,dy,False)
            elif map[by][bx] == ']':
                return True and check_vertical(bx-1,by,dx,dy,False)
        else:
            if map[by][bx] == '[':
                return check_vertical(bx+dx,by+dy,dx,dy,True) and check_vertical(bx+1,by,dx,dy,False)
            elif map[by][bx] == ']':
                return check_vertical(bx+dx,by+dy,dx,dy,True) and check_vertical(bx-1,by,dx,dy,False)
    else:
        if map[by+dy][bx+dx] == '.':
            return True
        else:
            return check_vertical(bx+dx,by+dy,dx,dy,True)
        
def move_vertical(bx,by,dx,dy,check):
    if check:
        if map[by+dy][bx+dx] == '.':
            map[by+dy][bx+dx] = map[by][bx]
            if map[by][bx] == '[':
                move_vertical(bx+1,by,dx,dy,False)
            elif map[by][bx] == ']':
                move_vertical(bx-1,by,dx,dy,False)
        else:
            if map[by][bx] == '[':
                move_vertical(bx+dx,by+dy,dx,dy,True)
                map[by+dy][bx+dx] = map[by][bx]
                move_vertical(bx+1,by,dx,dy,False)
            elif map[by][bx] == ']':
                move_vertical(bx+dx,by+dy,dx,dy,True)
                map[by+dy][bx+dx] = map[by][bx]
                move_vertical(bx-1,by,dx,dy,False)
            
    else:
        if map[by+dy][bx+dx] == '.':
            map[by+dy][bx+dx] = map[by][bx]
            map[by][bx] = '.'
        else:
            move_vertical(bx+dx,by+dy,dx,dy,True)
            map[by+dy][bx+dx] = map[by][bx]
            map[by][bx] = '.'
            


dirs = {'^':(0,-1),'>':(1,0),'v':(0,1),'<':(-1,0)}
counter = 0
for inst in instructions:
    dx,dy = dirs[inst]
    nx = px + dx
    ny = py + dy

    if map[ny][nx] == '.':
        px = nx
        py = ny
    # move horizontal
    elif map[ny][nx] in ['[',']'] and inst in ['<','>']:
        if move_horizontal(nx,ny,dx,dy):
            map[ny][nx] = '.'
            px = nx
            py = ny
    # move vertical
    elif map[ny][nx] in ['[',']'] and inst in ['^','v']:
        if check_vertical(nx,ny,dx,dy,True):
            move_vertical(nx,ny,dx,dy,True)
            if map[ny][nx] == '[':
                map[ny][nx+1] = '.'
            else:
                map[ny][nx-1] = '.'
            map[ny][nx] = '.'
            px = nx
            py = ny

    # with open(f'map_{counter}.txt','w') as f:
    #     for y in range(len(map)):
    #         for x in range(len(map[0])):
    #             if y == py and x == px:
    #                 f.write('@')
    #             else:
    #                 f.write(map[y][x])
    #         f.write('\n')
    # counter += 1

res = 0
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == '[':
            res += y*100 + x
print(res)