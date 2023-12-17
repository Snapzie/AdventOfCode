import numpy as np
# Part 1
# f = open('./input.txt','r').read().strip()
# arr = np.array([[c for c in line] for line in f.split('\n')])
# # print(arr)
# d = {'O':0,'.':1}

# # north 
# sorts = []
# for i in range(len(arr[0])):
#     col = ''.join(arr[:,i])
#     subs = col.split('#')
#     sorts.append('#'.join([''.join(sorted(sub,key=lambda x: d[x])) for sub in subs]))
# sorts = np.array([[c for c in line] for line in sorts]).T
# # print(sorts)

# res = 0
# for i,row in enumerate(sorts):
#     res += sum(row == 'O') * (len(sorts) - i)

# print(res)

# Part 2
f = open('./input.txt','r').read().strip()
arr = np.array([[c for c in line] for line in f.split('\n')])
# print(arr)
d = {'O':0,'.':1}

# north 
def tiltNorth(arr):
    sorts = []
    for i in range(len(arr[0])):
        col = ''.join(arr[:,i])
        subs = col.split('#')
        sorts.append('#'.join([''.join(sorted(sub,key=lambda x: d[x])) for sub in subs]))
    return np.array([[c for c in line] for line in sorts]).T

# West
def tiltWest(arr):
    sorts = []
    for row in arr:
        subs = ''.join(row).split('#')
        sorts.append('#'.join([''.join(sorted(sub,key=lambda x: d[x])) for sub in subs]))
    return np.array([[c for c in line] for line in sorts])

# South
def tiltSouth(arr):
    sorts = []
    for i in range(len(arr[0])):
        col = ''.join(arr[:,i])
        subs = col.split('#')
        sorts.append('#'.join([''.join(sorted(sub,key=lambda x: -d[x])) for sub in subs]))
    return np.array([[c for c in line] for line in sorts]).T

# East
def tiltEast(arr):
    sorts = []
    for row in arr:
        subs = ''.join(row).split('#')
        sorts.append('#'.join([''.join(sorted(sub,key=lambda x: -d[x])) for sub in subs]))
    return np.array([[c for c in line] for line in sorts])

prevs = []
for i in range(1000000000):
    prevs.append(arr)
    arr = tiltEast(tiltSouth(tiltWest(tiltNorth(arr))))
    if any([np.array_equal(arr,a) for a in prevs]):
        print([np.array_equal(arr,a) for a in prevs])
        print([np.array_equal(arr,a) for a in prevs].index(True))
        print(len([np.array_equal(arr,a) for a in prevs][:101]))
        break
arr = prevs[-1]
print(arr)
res = 0
for i,row in enumerate(arr):
    res += sum(row == 'O') * (len(arr) - i)
print(res)