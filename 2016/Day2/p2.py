from collections import defaultdict
lines = open('./input.txt').read().split('\n')
directions = {
    'U': ( 0,-1),
    'R': ( 1, 0),
    'L': (-1, 0),
    'D': ( 0, 1)
}
digits = defaultdict(lambda: -1,{
    (2,0): '1',
    (1,1): '2',
    (2,1): '3',
    (3,1): '4',
    (0,2): '5',
    (1,2): '6',
    (2,2): '7',
    (3,2): '8',
    (4,2): '9',
    (1,3): 'A',
    (2,3): 'B',
    (3,3): 'C',
    (2,4): 'D'
})
code = ''
pos = (0,2)
for line in lines:
    for inst in line:
        x,y = pos
        dx,dy = directions[inst]
        nx = x+dx
        ny = y+dy
        if digits[nx,ny] != -1:
            x = nx
            y = ny
        pos = (x,y)
    code = code + digits[pos]
print(code)
        