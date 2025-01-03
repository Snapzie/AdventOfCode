from collections import defaultdict
import copy

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
queue = [('R',px,py,0,[])]
seen = defaultdict(lambda: 10e10000000)
best_path_cost = 10e10000000
paths = set()
while len(queue):
    dir,px,py,score,path = queue.pop(0)
    if px == ex and py == ey:
        if score < best_path_cost:
            best_path_cost = score
        for path_x,path_y in path:
            paths.add((path_x,path_y))
        continue

    if seen[(dir,px,py)] < score or score > best_path_cost:
        continue
    
    path.append((px,py))
    for turn in [dir] + turns[dir]:
        dx,dy = dirs[dir]
        nx = px + dx
        ny = py + dy
        
        if turn == dir:
            if map[ny][nx] != '#':
                queue.append((dir,nx,ny,score+1,path.copy()))
        else:
            queue.append((turn,px,py,score+1000,path.copy()))
    
    seen[(dir,px,py)] = score
    
    
    queue.sort(key=lambda x: x[3])

paths.add((ex,ey))
print(len(paths))