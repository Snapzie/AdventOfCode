import numpy as np
np.set_printoptions(linewidth=100000)
f = open('./input.txt','r').read().strip()

data = np.array([[split for split in line.split()] for line in f.split('\n')])
dirs = data[:,0]
lengths = np.array(data[:,1],dtype=int)

# arr = np.full(((sum(lengths[dirs == 'U']))*2+1,(sum(lengths[dirs == 'R']))*2+1),0)
# y,x = sum(lengths[dirs == 'U'])*2 // 2, sum(lengths[dirs == 'R'])*2 // 2 

# for dir,length in zip(dirs,lengths):
#     if dir == 'R':
#         arr[y,x:x+length+1] = 1
#         x += length
#     if dir == 'D':
#         arr[y:y+length+1,x] = 1
#         y += length
#     if dir == 'U':
#         arr[y-length:y+1,x] = 1
#         y -= length
#     if dir == 'L':
#         arr[y,x-length:x+1] = 1
#         x -= length

# arrOrg = np.copy(arr)
# for i in range(len(arr)):
#     count = 0
#     idx = 0
#     while (idx < len(arr[0])-1):
#         if arr[i,idx] == 0:
#             if count % 2 == 0:
#                 pass
#             else:
#                 arr[i,idx] = 1
#             idx += 1
#         if arr[i,idx] == 1:
#             start = idx
#             while arr[i,idx] == 1:
#                 idx += 1
#             stop = idx-1
#             print(arrOrg[i-1,start],arrOrg[i+1,start],arrOrg[i+1,stop],arrOrg[i-1,stop])
#             if arrOrg[i-1,start] == 1 and arrOrg[i+1,start] == 0 and arrOrg[i+1,stop] == 0 and arrOrg[i-1,stop] == 1:
#                 pass
#             elif arrOrg[i+1,start] == 1 and arrOrg[i-1,start] == 0 and arrOrg[i-1,stop] == 0 and arrOrg[i+1,stop] == 1:
#                 pass
#             else:
#                 count += 1
            
# with open('./out2.txt','w') as f:
#     for row in arr:
#         for val in row:
#             f.write(str(val))
#         f.write('\n')
# print(arr.sum())


# Shoelace formula
coords = [(0,0)]
y,x = 0,0
for dir,length in zip(dirs,lengths):
    if dir == 'R':
        x += length-1
        coords.append((x,y))
    if dir == 'D':
        y -= length-1
        coords.append((x,y))
    if dir == 'U':
        y += length-1
        coords.append((x,y))
    if dir == 'L':
        x -= length-1
        coords.append((x,y))
# coords = coords + [(10,10)]
print(coords)
res = 0
for a,b in zip(coords[:-1],coords[1:]):
    res += (a[1]+b[1])*(a[0]-b[0])
# res += (coords[-1][0]+coords[0][0])*(coords[-1][1]-coords[0][1])
print(res)