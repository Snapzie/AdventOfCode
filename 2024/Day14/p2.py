# 100379268 low

import re
from collections import defaultdict

seconds = 100000000
height = 103
width = 101

robots = []
instructions = open('input.txt').read().split('\n')
for inst in instructions:
    matches = re.findall('\d+|-\d+',inst)
    x,y,vx,vy = map(lambda x: int(x),matches)
    robots.append({
        'x': x,
        'y': y,
        'vx': vx,
        'vy': vy
    })

img = [['.' for _ in range(width)] for _ in range(height)]
for robot in robots:
    x,y,vx,vy = robot['x'],robot['y'],robot['vx'],robot['vy']
    px = (x + vx*7672) % width
    py = (y + vy*7672) % height
    img[py][px] = '#'
with open('out.txt','w') as f:
    for y in range(len(img)):
        for x in range(len(img[0])):
            f.write(img[y][x])
        f.write('\n')



print(len(robots))
for i in range(101*103+1):
    y_dict = defaultdict(lambda: set())
    x_dict = defaultdict(lambda: set())
    for robot in robots:
        x,y,vx,vy = robot['x'],robot['y'],robot['vx'],robot['vy']
        fx = (x + vx*i) % width
        y_dict[(y + vy*i) % height].add(fx)

    for k,v in y_dict.items():
        if len(v) >= 32:
            print(f'{i}: {k},{len(v)}')