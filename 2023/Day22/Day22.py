import numpy as np
f = open('./input2.txt','r').read().strip()
coords = np.array([[[int(c) for c in s.split(',')][::-1] for s in line.split('~')] for line in f.split('\n')])
# coords = np.array(sorted(coords,key=lambda x: np.max(x[:,0])))
sx = np.max(coords[:,:,2])+1
sy = np.max(coords[:,:,1])+1
sz = np.max(coords[:,:,0])+2
arr = np.full((sz,sy,sx),-1)
arr[0,:,:] = -2
arr[-1,:,:] = -2

for i,coord in enumerate(coords):
    start = coord[0]
    end = coord[1] + 1
    arr[start[0]:end[0],start[1]:end[1],start[2]:end[2]] = i
    
moving = True
while moving:
    # coords = np.array(sorted(coords,key=lambda x: np.max(x[:,0])))
    moving = False
    for i,coord in enumerate(coords):
        start = coord[0]
        end = coord[1] + 1
        # n = arr[start[0],start[1],start[2]]
        n=i

        # Slice below
        slice = arr[start[0]-1:end[0]-1,start[1]:end[1],start[2]:end[2]].flatten()
        vals = np.delete(slice,np.argwhere(slice==n))
        if all([v == -1 for v in vals]):
            moving = True
            # updating tower
            arr[start[0]:end[0],start[1]:end[1],start[2]:end[2]] = -1
            arr[start[0]-1:end[0]-1,start[1]:end[1],start[2]:end[2]] = n

            # updating coords
            end = end - 1
            coords[i,0] = [start[0]-1,start[1],start[2]]
            coords[i,1] = [end[0]-1,end[1],end[2]]

with open('./out.txt','w') as f:
    for z in arr:
        for y in z:
            for x in y:
                f.write(f'{x:5.0f}')
            f.write('\n')
        f.write('\n')
res = 0
for i,coord in enumerate(coords):
    start = coord[0]
    end = coord[1] + 1
    # n = arr[start[0],start[1],start[2]]
    n=i
    # Slice above
    slice = arr[start[0]+1:end[0]+1,start[1]:end[1],start[2]:end[2]].flatten()
    vals = np.delete(slice,np.argwhere((slice==n) | (slice==-1) | (slice==-2)))
    if len(vals) == 0:
        print(n,'true')
        res += 1
        continue
    else:
        distinct = np.unique(vals)
        # print(n)
        # print(distinct)
        reliance = []
        for d in distinct:
            vals = []
            # print(np.argwhere(arr == d))
            for coords in np.argwhere(arr[start[0]+1,:,:] == d):
                y,x = coords
                # print(arr[z-1,y,x])
                vals.append(arr[start[0],y,x])
            reliance.append( not any([v not in [n,-1,-2] for v in vals]))
        if not any(reliance):
            print(n,'true')
            res += 1
        else:
            print(n,'false')
print(res)
# 427 - low
# 500 - high
# 440 - high
# 428 - %
# 429 - %
# 430 - %
# 431 - %
# 432 - %
# 433 - %
# 434 - %
# 435 - %
# 436 - %
# 437 - %
# 438 - %