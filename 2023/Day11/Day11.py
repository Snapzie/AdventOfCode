# Part 1
import numpy as np

f = open('input2.txt','r').read().strip()
universe = np.array([[c for c in line] for line in f.split('\n')])

for i in range(len(universe[0])-2,-1,-1):
    slice = universe[:,i+1]
    if all(slice == '.'):
        universe = np.insert(universe,i+1,'.',axis=1)
for i in range(len(universe)-2,-1,-1):
    slice = universe[i+1,:]
    if all(slice == '.'):
        universe = np.insert(universe,i+1,'.',axis=0)
print(universe)

coords = []
for i,l in enumerate(universe):
    for j,e in enumerate(l):
        if e == '#':
            coords.append((i,j))

dists = []
for i in range(len(coords)):
    for j in range(i+1,i+len(coords[i+1:])+1):
        ay,ax = coords[i]
        by,bx = coords[j]
        dists.append(abs((by-ay))+abs((bx-ax)))
print(sum(dists))

# Part 2
import numpy as np

f = open('input2.txt','r').read().strip()
universe = np.array([[c for c in line] for line in f.split('\n')])
print(universe)

coords = []
for i,l in enumerate(universe):
    for j,e in enumerate(l):
        if e == '#':
            coords.append((i,j))

dists = []
for i in range(len(coords)):
    for j in range(i+1,i+len(coords[i+1:])+1):
        ay,ax = coords[i]
        by,bx = coords[j]
        hoz = sorted([ax,bx])
        vert = sorted([ay,by])

        empty = 0
        for h in range(hoz[0],hoz[1]+1):
            if all(universe[:,h] == '.'):
                empty += 1
        for v in range(vert[0],vert[1]+1):
            if all(universe[v,:] == '.'):
                empty += 1
        dists.append(abs(ax-bx)+abs(ay-by)+(empty*999999))
print(sum(dists))