map = [[int(char) for char in l] for l in open('input.txt').read().split('\n')]

starting_pos = []
for y in range(len(map)):
    for x in range(len(map[0])):
        if map[y][x] == 0:
            starting_pos.append((x,y))

dirs = [(0,-1),(1,0),(0,1),(-1,0)]
res = 0
for x,y in starting_pos:
    queue = [(x,y,0,((x,y)))]
    rating = set()
    while len(queue) > 0:
        x,y,val,path = queue.pop(0)
        if map[y][x] == 9:
            rating.add(path)
            continue
        for dx,dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < len(map[0]) and 0 <= ny < len(map) and map[ny][nx] == val+1:
                queue.append((nx,ny,val+1,path+(nx,ny)))
    res += len(rating)
print(res)