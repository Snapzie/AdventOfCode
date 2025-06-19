# 220 low
seq = list(map(lambda x: x.strip(),open('./input.txt','r').read().split(',')))
dir = {
    'R': ( 1,0),
    'L': (-1,0)
}
prev_pos = set()
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
    elif o == 3:
        tmp = dx
        dx = dy
        dy = tmp

    if dx == 0:
        args = [1,dy*b+1,1] if dy*b > 0 else [-1,dy*b-1,-1]
        rng = [(x,y+i) for i in range(*args)]
    else:
        args = [1,dx*b+1,1] if dx*b > 0 else [-1,dx*b-1,-1]
        rng = [(x+i,y) for i in range(*args)]
    for r in rng:
        # print(sorted(prev_pos))
        if r in prev_pos:
            print(r)
        prev_pos.add(r)

    x = x + dx*b
    y = y + dy*b

    if d == 'R':
        o = (o+1)%4
    if d == 'L':
        o = (o-1)%4
    pos = (o,x,y)