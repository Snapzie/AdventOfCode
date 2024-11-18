import numpy as np
np.set_printoptions(linewidth=100000)
f = open('./input.txt','r').read().strip()

data = np.array([[split for split in line.split()] for line in f.split('\n')])
dirs = data[:,0]
lengths = np.array(data[:,1],dtype=int)

x,y = 0,0
coords = [(x,y)]
for dir,length in zip(dirs,lengths):
    if dir == 'R':
        x = x + length
        coords.append((x,y))
    if dir == 'D':
        y = y - length
        coords.append((x,y))
    if dir == 'L':
        x = x - length
        coords.append((x,y))
    if dir == 'U':
        y = y + length
        coords.append((x,y))

print(coords)

# coords = coords[::-1]
A = 0
for p1,p2 in zip(coords[:-1],coords[1:]):
    x_diff = p1[0]-p2[0]
    y_diff = p1[1]+p2[1]
    print(y_diff*x_diff*0.5)
    A += y_diff*x_diff*0.5
print(A)