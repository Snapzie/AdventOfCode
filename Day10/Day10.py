# f = open('./input.txt','r').read().strip()
# pipeMap = [res for res in f.split('\n')]
# placeholder = 99
# pathMap = [[placeholder] * len(pipeMap[0]) for _ in range(len(pipeMap))]
# d = {'-':[(0,-1),(0,1)],'|':[(1,0),(-1,0)],'7':[(1,0),(0,-1)],'F':[(1,0),(0,1)],'J':[(-1,0),(0,-1)],'L':[(-1,0),(0,1)],'.':[]}

# sy,sx = 0,0
# for i,l in enumerate(pipeMap):
#     for j,e in enumerate(l):
#         if e == 'S':
#             sy,sx = i,j

# pathMap[sy][sx] = 0

# matches = []
# directions = [(-1,0),(0,1),(1,0),(0,-1)]
# for k in d.keys():
#     counter = 0
#     for dy,dx in directions:
#         if (dy,dx) in d[k] and (-dy,-dx) in d[pipeMap[sy+dy][sx+dx]]:
#             counter += 1
#     matches.append((k,counter))

# openList = [(sy+a,sx+b) for a,b in d[sorted(matches,key=lambda x: x[1])[-1][0]]]
# for y,x in openList:
#     pathMap[y][x] = 1
# closedList = [(sy,sx)]

# while len(openList) > 0:
#     y,x = openList.pop()
#     cost = pathMap[y][x]+1
#     for ry,rx in d[pipeMap[y][x]]:
#         if pathMap[y+ry][x+rx] <= cost:
#             continue
#         else:
#             openList.append((y+ry,x+rx))
#             pathMap[y+ry][x+rx] = cost
#     # closedList.append((y,x))
# res = 0
# for l in pathMap:
#     for e in l:
#         res = e if e > res and e != placeholder else res
# print(res)
# for l in pathMap:
#     print(f'{l}\n')

# Part 2
import numpy as np
np.set_printoptions(suppress=True, linewidth=100000)

def replaceS(y,x,d,map):
    matches = []
    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    for k in d.keys():
        counter = 0
        for dy,dx in directions:
            if (dy,dx) in d[k] and (-dy,-dx) in d[map[y+dy][x+dx]]:
                counter += 1
        matches.append((k,counter))
    return sorted(matches,key=lambda x: x[1])[-1][0]

f = open('./input.txt','r').read().strip()
pipeMap = [res for res in f.split('\n')]
placeholder = 1e5
pathMap = [[placeholder] * len(pipeMap[0]) for _ in range(len(pipeMap))]
d = {'-':[(0,-1),(0,1)],'|':[(1,0),(-1,0)],'7':[(1,0),(0,-1)],'F':[(1,0),(0,1)],'J':[(-1,0),(0,-1)],'L':[(-1,0),(0,1)],'S':[],'*':[],'/':[],'.':[]}

# Find initial S
sy,sx = 0,0
for i,l in enumerate(pipeMap):
    for j,e in enumerate(l):
        if e == 'S':
            sy,sx = i,j

pathMap[sy][sx] = 0
openList = [(sy+a,sx+b) for a,b in d[replaceS(sy,sx,d,pipeMap)]]
for y,x in openList:
    pathMap[y][x] = 1
closedList = [(sy,sx)]

# create pathMap
while len(openList) > 0:
    y,x = openList.pop()
    cost = pathMap[y][x]+1
    for ry,rx in d[pipeMap[y][x]]:
        if pathMap[y+ry][x+rx] <= cost:
            continue
        else:
            openList.append((y+ry,x+rx))
            pathMap[y+ry][x+rx] = cost
    # closedList.append((y,x))

# SDF = np.zeros((len(pathMap),len(pathMap[0])),dtype=str)
SDF = np.full((len(pathMap),len(pathMap[0])),'*',dtype=str)

# Insert pipes into SDF
for i,l in enumerate(pathMap):
    for j,e in enumerate(l):
        if e != placeholder:
            SDF[i,j] = pipeMap[i][j]

# Replace initial S
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e == 'S':
            SDF[i,j] = replaceS(i,j,d,SDF)

# Insert column spaces
for i in range(len(SDF[0])-2,-1,-1):
    rc = [a[i+1] for a in SDF]
    lc = [a[i] for a in SDF]
    for rv,lv in zip(rc,lc):
        if rv in ['F','|','L'] and lv in ['J','7','|']:
            a = ['S' for _ in range(len(SDF))]
            # a[0] = '.'
            # a[-1] = '.'
            SDF = np.insert(SDF,i+1,a,axis=1)
            break

# Add boundary
SDF = np.pad(SDF,1,constant_values='.')
# Replace all inserted S
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e == 'S':
            SDF[i,j] = replaceS(i,j,d,SDF)

# # Insert row spaces
# for i,l in enumerate(SDF):
#     for j,e in enumerate(l):
#         if SDF[i-1][j] in ['L','J','-'] and SDF[i][j] in ['-','7','F']:
#             a = ['S' for _ in range(len(SDF[0]))]
#             # a[0] = '.'
#             # a[-1] = '.'
#             SDF = np.insert(SDF,i,a,axis=0)

# Insert row spaces
for i in range(len(SDF)-2,-1,-1):
    br = SDF[i+1]
    tr = SDF[i]
    for tv,bv in zip(tr,br):
        if tv in ['L','J','-'] and bv in ['-','7','F']:
            a = ['S' for _ in range(len(SDF[0]))]
            # a[0] = '.'
            # a[-1] = '.'
            SDF = np.insert(SDF,i+1,a,axis=0)
            break

# Add boundary
SDF = np.pad(SDF,1,constant_values='/')

# Replace all inserted S
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e == 'S':
            SDF[i,j] = replaceS(i,j,d,SDF)

# Find all potential pocket locations
stars = []
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e == '*':
            stars.append((i,j))

# Compute pockets
for sy,sx in stars:
    openList = [(sy,sx)]
    closedList = []
    looping = True
    while looping:
        if len(openList) == 0:
            SDF[sy,sx] = 'I'
            break
        y,x = openList.pop()
        closedList.append((y,x))
        for ry,rx in [(-1,0),(0,1),(1,0),(0,-1)]:
            if SDF[y+ry,x+rx] == '/':
                SDF[sy,sx] = 'O'
                looping = False
                break
            elif SDF[y+ry,x+rx] in ['*','.','O','I'] and (y+ry,x+rx) not in closedList:
                openList.append((y+ry,x+rx))
            else:
                continue

# Replace pipes with X
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e in ['-','|','L','J','F','7']:
            SDF[i,j] = 'X'
print(SDF)

# Count pockets
res = 0
for i,l in enumerate(SDF):
    for j,e in enumerate(l):
        if e == 'I':
            res += 1

# Draw map to out.txt
with open('./out.txt','w') as f:
    for l in SDF:
        for e in l:
            f.write(e)
        f.write('\n')
print(res)