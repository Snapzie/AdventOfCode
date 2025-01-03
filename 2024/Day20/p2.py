map = [[c for c in l] for l in open('input.txt').read().split('\n')]

for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 'S':
            px = x
            py = y
        if map[y][x] == 'E':
            ex = x
            ey = y

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
dict = {}
queue = [(px,py,0)]
seen = set()
while len(queue) > 0:
    px,py,steps = queue.pop()
    dict[(px,py)] = steps
    for dx,dy in dirs:
        nx = px + dx
        ny = py + dy
        if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] != '#' and (nx,ny) not in seen:
            queue.append((nx,ny,steps+1))
    seen.add((px,py))

dirs = set()
n = 21
for i in range(n):
    for j in range(n-i):
        dirs.add((j,i))
        dirs.add((-j,i))
        dirs.add((j,-i))
        dirs.add((-j,-i))
res = 0
for (px,py),v in dict.items():
    for dx,dy in dirs:
        nx = px + dx
        ny = py + dy
        if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] != '#':
            c_val = dict[(px,py)]
            n_val = dict[(nx,ny)]
            if n_val > c_val and n_val-c_val-(abs(dx)+abs(dy)) >= 100:
                # print(n_val-c_val-2)
                res += 1
print(res)