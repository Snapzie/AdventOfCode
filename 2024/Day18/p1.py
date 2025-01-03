# 140 - low

from collections import defaultdict

bytes = [(int(l.split(',')[0]),int(l.split(',')[1])) for l in open('input.txt').read().split('\n')]
width = 71
height = 71
map = [['.' for _ in range(width)] for _ in range(height)]
for _ in range(1024):
    x,y = bytes.pop(0)
    map[y][x] = '#'

dirs = [(0,-1),(1,0),(0,1),(-1,0)]


def find_path():
    queue = [(0,0,0)]
    seen = defaultdict(lambda: 10e1000000)
    while len(queue) > 0:
        px,py,steps = queue.pop(0)
        if px == 70 and py == 70:
            return True

        if seen[(px,py)] <= steps:
            continue

        for dx,dy in dirs:
            nx = px + dx
            ny = py + dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] != '#':
                queue.append((nx,ny,steps+1))
        seen[(px,py)] = steps
    return False

while True:
    if not find_path():
        print(x,y)
        break
    x,y = bytes.pop(0)
    map[y][x] = '#'
