import numpy as np

# Part 1
res = []
grid = np.loadtxt("input.txt",dtype=str,comments=None)
grid = np.array(list(map(lambda x: [[char] for char in x],grid)))
print(grid.shape)
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if not grid[y,x,0].isnumeric() and grid[y,x] != '.':
            print(grid[y,x])
            print(f'''{grid[y-1,x-1]},{grid[y-1,x]},{grid[y-1,x+1]}\n
{grid[y,x-1]},{grid[y,x]},{grid[y,x+1]}\n
{grid[y+1,x-1]},{grid[y+1,x]},{grid[y+1,x+1]}
            ''')
            gridsToCheck = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
            numsFound = []
            for vy,vx in gridsToCheck:
                if grid[vy,vx,0].isnumeric():
                    num = grid[vy,vx,0]

                    checkLeft = vx
                    while (checkLeft >= 0):
                        checkLeft -= 1
                        if grid[vy,checkLeft,0].isnumeric():
                            num = grid[vy,checkLeft,0]+num
                        else:
                            break
                    checkright = vx
                    while (checkright < grid.shape[1]-1):
                        checkright += 1
                        if grid[vy,checkright,0].isnumeric():
                            num = num+grid[vy,checkright,0]
                        else:
                            break
                    numsFound.append(int(num))
            print(np.unique(numsFound))
            res.append(np.unique(numsFound))   
print(sum(np.hstack(res)))

# Part 2
res = []
grid = np.loadtxt("input.txt",dtype=str,comments=None)
grid = np.array(list(map(lambda x: [[char] for char in x],grid)))
print(grid.shape)
for y in range(grid.shape[0]):
    for x in range(grid.shape[1]):
        if grid[y,x,0]== '*':
            print(grid[y,x])
            print(f'''{grid[y-1,x-1]},{grid[y-1,x]},{grid[y-1,x+1]}\n
{grid[y,x-1]},{grid[y,x]},{grid[y,x+1]}\n
{grid[y+1,x-1]},{grid[y+1,x]},{grid[y+1,x+1]}
            ''')
            gridsToCheck = [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]
            numsFound = []
            for vy,vx in gridsToCheck:
                if grid[vy,vx,0].isnumeric():
                    num = grid[vy,vx,0]

                    checkLeft = vx
                    while (checkLeft >= 0):
                        checkLeft -= 1
                        if grid[vy,checkLeft,0].isnumeric():
                            num = grid[vy,checkLeft,0]+num
                        else:
                            break
                    checkright = vx
                    while (checkright < grid.shape[1]-1):
                        checkright += 1
                        if grid[vy,checkright,0].isnumeric():
                            num = num+grid[vy,checkright,0]
                        else:
                            break
                    numsFound.append(int(num))
            uniques = np.unique(numsFound)
            if len(uniques) == 2:
                res.append(uniques[0] * uniques[1])   
print(sum(np.hstack(res)))
            