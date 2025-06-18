# 220 low
seq = list(map(lambda x: x.strip(),open('./input.txt','r').read().split(',')))
dir = {
    'R': ( 1,0),
    'L': (-1,0)
}
pos = (0,0,0)
for inst in seq:
    d = inst[0]
    b = int(inst[1:])
    o,x,y = pos
    dx,dy = dir[d]
    if o == 1:
        tmp = dx
        dx = dy*-1
        dy = tmp*-1
    elif o == 2:
        dx *= -1
    elif 0 == 3:
        tmp = dx
        dx = dy
        dy = tmp
    # print(o,x,y,dx,dy,b)
    x = x + dx*b
    y = y + dy*b

    if d == 'R':
        o = (o+1)%4
    if d == 'L':
        o = (o-1)%4
    pos = (o,x,y)
print(pos)
_,x,y = pos
print(abs(x)+abs(y))