import numpy as np

# part 1
# f = open('./input.txt','r').read().strip()
# garden = np.array([[c for c in line] for line in f.split('\n')])
# print(garden)

# start = (0,0)
# for i,row in enumerate(garden):
#     for j,c in enumerate(row):
#         if c == 'S':
#             start = (i,j)
# print(start)

# openList = [start]
# for n in range(64):
#     mark = 'U' if n % 2 == 0 else 'E'
#     newList = []
#     for y,x in openList:
#         for ry,rx in [(0,1),(1,0),(0,-1),(-1,0)]: # R,D,L,U
#             # out of bounds
#             if y+ry < 0 or y+ry >= len(garden) or x+rx < 0 or x+rx >= len(garden[0]):
#                 continue
#             if garden[y+ry,x+rx] == '.':
#                 garden[y+ry,x+rx] = mark
#                 newList.append((y+ry,x+rx))
#     openList = list(newList)

# res = 0
# for row in garden:
#     for c in row:
#         if c == 'E':
#             res += 1
# print(res + 1)

# with open('./out.txt','w') as f:
#     for row in garden:
#         for c in row:
#             f.write(c)
#         f.write('\n')

# part 2
f = open('./input3.txt','r').read().strip()
garden = np.array([[c for c in line] for line in f.split('\n')])
print(garden)

start = (0,0)
for i,row in enumerate(garden):
    for j,c in enumerate(row):
        if c == 'S':
            start = (i,j)
print(start)

openList = [start]
for n in range(22):
    mark = 'U' if n % 2 == 0 else 'E'
    newList = []
    for y,x in openList:
        for ry,rx in [(0,1),(1,0),(0,-1),(-1,0)]: # R,D,L,U
            # out of bounds
            if y+ry < 0 or y+ry >= len(garden) or x+rx < 0 or x+rx >= len(garden[0]):
                continue
            if garden[y+ry,x+rx] == '.':
                garden[y+ry,x+rx] = mark
                newList.append((y+ry,x+rx))
    openList = list(newList)

res = 0
for row in garden:
    for c in row:
        if c == 'E':
            res += 1
print(res + 1)

with open('./out.txt','w') as f:
    for row in garden:
        for c in row:
            f.write(c)
        f.write('\n')
