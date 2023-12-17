import numpy as np
f = open('./input.txt','r').read().strip()
mirrors = np.array([[c for c in line] for line in f.split('\n')])
energized = np.zeros(mirrors.shape)
print(mirrors)
print(energized)

dirs = {'D':(1,0),'U':(-1,0),'L':(0,-1),'R':(0,1)}
d = {
    '\\': {
        'D':((0,1),'R'),
        'U':((0,-1),'L'),
        'L':((-1,0),'D'),
        'R':((1,0),'U')
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
        'L':((0,-1),'L'),
        'R':((0,1),'R')
    },
    '|':{
        'D':((1,0),'D'),
        'U':((-1,0),'U'),
        'L':[((-1,0),'U'),((1,0),'D')],
        'R':[((-1,0),'U'),((1,0),'U')]
    }
}

l = [((0,0),'R')]
while len(l) > 0:
    (y,x),d = l.pop(0)
    if mirrors[y,x] == '.':
        ry,rx = dirs[d]
        l.append(((y+ry,x+rx),d))
    print(y,x,d)