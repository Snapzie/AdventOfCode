# Part 1
# import numpy as np
# f = open('./input2.txt','r').read().strip()
# mirrors = np.array([[c for c in line] for line in f.split('\n')])
# energized = np.zeros(mirrors.shape)
# mirrors = np.pad(mirrors,(1,1),constant_values='0')
# energized = np.pad(energized,(1,1),constant_values=0)
# # print(mirrors)
# # print(energized)

# dirs = {'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
# mirrorDict = {
#     '\\': {
#         'D':((0,1),'R'),
#         'U':((0,-1),'L'),
#         'L':((-1,0),'U'),
#         'R':((1,0),'D')
#     },
#     '/':{
#         'D':((0,-1),'L'),
#         'U':((0,1),'R'),
#         'L':((1,0),'D'),
#         'R':((-1,0),'U')
#     },
#     '-':{
#         'D':[((0,-1),'L'),((0,1),'R')],
#         'U':[((0,-1),'L'),((0,1),'R')],
#         'L':[((0,-1),'L')],
#         'R':[((0,1),'R')]
#     },
#     '|':{
#         'D':[((1,0),'D')],
#         'U':[((-1,0),'U')],
#         'L':[((-1,0),'U'),((1,0),'D')],
#         'R':[((-1,0),'U'),((1,0),'D')]
#     }
# }
# count = 0
# l = [((1,1),'R')]
# closedList = []
# while len(l) > 0:
#     (y,x),dir = l.pop(0)
#     if ((y,x),dir) in closedList:
#         continue
#     mirror = mirrors[y,x]

#     if mirror == '0':
#         continue

#     if mirror == '.':
#         # if energized[y,x] == 2:
#         #     continue
#         ry,rx = dirs[dir]
#         l.append(((y+ry,x+rx),dir))
#     if mirror == '|':
#         vals = mirrorDict[mirror][dir]
#         for v in vals:
#             (ry,rx),nd = v
#             l.append(((y+ry,x+rx),nd))
#     if mirror == '-':
#         vals = mirrorDict[mirror][dir]
#         for v in vals:
#             (ry,rx),nd = v
#             l.append(((y+ry,x+rx),nd))
#     if mirror == '/':
#         (ry,rx),nd = mirrorDict[mirror][dir]
#         l.append(((y+ry,x+rx),nd))
#     if mirror == '\\':
#         (ry,rx),nd = mirrorDict[mirror][dir]
#         l.append(((y+ry,x+rx),nd))
    
#     energized[y,x] = 1
#     closedList.append(((y,x),dir))
# print(energized.sum())
    
# Part 2
import numpy as np
f = open('./input2.txt','r').read().strip()
mirrors = np.array([[c for c in line] for line in f.split('\n')])
energized = np.zeros(mirrors.shape)
mirrors = np.pad(mirrors,(1,1),constant_values='0')
energized = np.pad(energized,(1,1),constant_values=0)
# print(mirrors)
# print(energized)

dirs = {'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
mirrorDict = {
    '\\': {
        'D':((0,1),'R'),
        'U':((0,-1),'L'),
        'L':((-1,0),'U'),
        'R':((1,0),'D')
    },
    '/':{
        'D':((0,-1),'L'),
        'U':((0,1),'R'),
        'L':((1,0),'D'),
        'R':((-1,0),'U')
    },
    '-':{
        'D':[((0,-1),'L'),((0,1),'R')],
        'U':[((0,-1),'L'),((0,1),'R')],
        'L':[((0,-1),'L')],
        'R':[((0,1),'R')]
    },
    '|':{
        'D':[((1,0),'D')],
        'U':[((-1,0),'U')],
        'L':[((-1,0),'U'),((1,0),'D')],
        'R':[((-1,0),'U'),((1,0),'D')]
    }
}

top = list(zip([(1,j) for j in np.arange(1,len(mirrors[0])-1)],['D']*(len(mirrors[0])-1))) + [((1,1),'R'),((1,len(mirrors[0])-2),'L')]
right = list(zip([(i,1) for i in np.arange(2,len(mirrors)-2)], ['R']*(len(mirrors[0])-1)))
left = list(zip([(i,len(mirrors[0])-2) for i in np.arange(2,len(mirrors)-2)], ['L']*(len(mirrors[0])-1)))
bottom = list(zip([(len(mirrors)-2,j) for j in np.arange(1,len(mirrors[0])-1)],['U']*(len(mirrors[0])-1))) + [((len(mirrors)-2,1),'R'),((len(mirrors)-2,len(mirrors[0])-2),'L')]

res = 0
for start in top + right + left + bottom:
    l = [start]
    closedList = []
    energized = np.zeros(mirrors.shape)
    energized = np.pad(energized,(1,1),constant_values=0)
    while len(l) > 0:
        (y,x),dir = l.pop(0)
        if ((y,x),dir) in closedList:
            continue
        mirror = mirrors[y,x]

        if mirror == '0':
            continue

        if mirror == '.':
            # if energized[y,x] == 2:
            #     continue
            ry,rx = dirs[dir]
            l.append(((y+ry,x+rx),dir))
        if mirror == '|':
            vals = mirrorDict[mirror][dir]
            for v in vals:
                (ry,rx),nd = v
                l.append(((y+ry,x+rx),nd))
        if mirror == '-':
            vals = mirrorDict[mirror][dir]
            for v in vals:
                (ry,rx),nd = v
                l.append(((y+ry,x+rx),nd))
        if mirror == '/':
            (ry,rx),nd = mirrorDict[mirror][dir]
            l.append(((y+ry,x+rx),nd))
        if mirror == '\\':
            (ry,rx),nd = mirrorDict[mirror][dir]
            l.append(((y+ry,x+rx),nd))
        
        energized[y,x] = 1
        closedList.append(((y,x),dir))
    if energized.sum() > res:
        res = energized.sum()
print(res)