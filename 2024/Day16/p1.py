from collections import defaultdict

map = [[c for c in l] for l in open('input.txt').read().split('\n')]
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 'S':
            px = x
            py = y
        if map[y][x] == 'E':
            ex = x
            ey = y

turns = {'U':['L','R'],'R':['U','D'],'D':['R','L'],'L':['U','D']}
dirs = {'U':(0,-1),'R':(1,0),'D':(0,1),'L':(-1,0)}
queue = [('R',px,py,0)]
seen = defaultdict(lambda: 10e10000000)
while True:
    dir,px,py,score = queue.pop(0)
    if px == ex and py == ey:
        print(score)
        break

    if seen[(dir,px,py)] <= score:
        continue
    
    for turn in [dir] + turns[dir]:
        dx,dy = dirs[dir]
        nx = px + dx
        ny = py + dy
        
        if turn == dir:
            if map[ny][nx] != '#':
                queue.append((dir,nx,ny,score+1))
        else:
            queue.append((turn,px,py,score+1000))
    
    seen[(dir,px,py)] = score
    
    queue.sort(key=lambda x: x[3])