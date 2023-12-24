import numpy as np

f = open('./input2.txt','r').read().strip()
arr = np.array(list(map(lambda x: [[int(i) for i in x[0].split(', ')],[int(j) for j in x[1].split(', ')]],[[res for res in line.split('@')] for line in f.split('\n')])))

pos = arr[:,0,:2]
velo = arr[:,1,:2]

coords = [(a,[a[0]+(b[0]*27),a[1]+(b[1]*27)]) for a,b in zip(pos,velo)]
posVelo = [(a,b) for a,b in zip(pos,velo)]

def intersection(l1,l2):
    a1 = l1[0]
    a2 = l1[1]
    b1 = l2[0]
    b2 = l2[1]
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

res = 0
for i,l1 in enumerate(coords[:-1]):
    for j,l2 in enumerate(coords[i+1:]):
        int_x,int_y = intersection(l1,l2)
        if (200000000000000 <= int_x <= 400000000000000) and (200000000000000 <= int_y <= 400000000000000):
        # if (7 <= int_x <= 27) and (7 <= int_y <= 27):
            # print(posVelo[i][0][0],posVelo[i][0][1])
            # print(posVelo[i][1][0],posVelo[i][1][1])
            if (posVelo[i][0][0] < int_x and posVelo[i][1][0] < 0) or (posVelo[i][0][0] > int_x and posVelo[i][1][0] > 0):# or (posVelo[i][0][1] < int_y and posVelo[i][1][1] < 0) or (posVelo[i][0][1] > int_y and posVelo[i][1][1] > 0):
                continue
            if (posVelo[j+i][0][0] < int_x and posVelo[j+i][1][0] < 0) or (posVelo[j+i][0][0] > int_x and posVelo[j+i][1][0] > 0):# or (posVelo[j+i][0][1] < int_y and posVelo[j+i][1][1] < 0) or (posVelo[j+i][0][1] > int_y and posVelo[j+i][1][1] > 0):
                continue
            res += 1
print(res)

# 7921 - low
# 17464 - low