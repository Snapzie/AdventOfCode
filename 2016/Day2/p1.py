lines = open('./input.txt').read().split('\n')
directions = {
    'U': ( 0,-1),
    'R': ( 1, 0),
    'L': (-1, 0),
    'D': ( 0, 1)
}
digits = {
    (0,0): '1',
    (1,0): '2',
    (2,0): '3',
    (0,1): '4',
    (1,1): '5',
    (2,1): '6',
    (0,2): '7',
    (1,2): '8',
    (2,2): '9'
}
code = ''
pos = (1,1)
for line in lines:
    for inst in line:
        x,y = pos
        dx,dy = directions[inst]
        x = min(max(x+dx,0),2)
        y = min(max(y+dy,0),2)
        pos = (x,y)
    code = code + digits[pos]
print(code)
        