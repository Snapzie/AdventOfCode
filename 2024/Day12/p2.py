# 889857 - low
# 921636

garden = [[c for c in l] for l in open('input.txt').read().split('\n')]

cost = 0
dirs = [(0,-1),(1,0),(0,1),(-1,0)]
seen = set()
for y in range(len(garden)):
    for x in range(len(garden[0])):
        if (x,y) in seen:
            continue
        print(garden[y][x])
        sides = 0
        area = 0
        queue = [(x,y)]
        shape = []
        while len(queue) > 0:
            px,py = queue.pop(0)
            if (px,py) in seen:
                continue
            for dx,dy in dirs:
                nx = px + dx
                ny = py + dy
                if 0 <= nx < len(garden[0]) and 0 <= ny < len(garden) and garden[ny][nx] == garden[py][px]:                    
                    queue.append((nx,ny))
            area += 1
            seen.add((px,py))
            shape.append((px,py))

        shape.sort(key=lambda x: (x[1],x[0]))
        # print(shape)
        prev_y = -1
        lock = {(0,-1): False,(1,0):False,(0,1):False,(-1,0):False}
        for px,py in shape:
            if py != prev_y:
                prev_y = py
                lock = {(0,-1): False,(1,0):False,(0,1):False,(-1,0):False}
            # up / down
            for dx,dy in [(0,-1),(0,1)]:
                nx = px + dx
                ny = py + dy
                if (not (0 <= ny < len(garden)) or garden[ny][nx] != garden[py][px]):
                    if lock[(dx,dy)] == False:
                        print(f'top/bottom: {dy}')
                        sides += 1
                        lock[(dx,dy)] = True
                    elif 0 <= px < len(garden[0]) and garden[py][px-1] != garden[py][px]:
                        print(f'top/bottom: {dy}')
                        sides += 1
                        lock[(dx,dy)] = True
                elif 0 <= ny < len(garden) and garden[ny][nx] == garden[py][px]:
                    lock[(dx,dy)] = False
                    
            # left
            for dx,dy in [(-1,0),(1,0)]:
                nx = px + dx
                ny = py + dy
                if not (0 <= nx < len(garden[0])) or garden[ny][nx] != garden[py][px]:
                    if not (0 <= py-1 < len(garden)) or garden[py-1][px] != garden[py][px]:
                        print(f'left/right: {dx}')
                        sides += 1
                    # left
                    elif 0 <= py-1 < len(garden) and 0 <= nx < len(garden[0]) and garden[py-1][nx] == garden[py][px]:
                        print(f'left/right: {dx}')
                        sides += 1


        print(f'cost: {sides*area}, sides: {sides}, area: {area}')
        cost += sides * area
print(cost)
        