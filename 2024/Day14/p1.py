# 100379268 low

import re

seconds = 100
height = 103
width = 101
mid_height = height // 2
mid_width = width // 2

q1,q2,q3,q4 = 0,0,0,0
instructions = open('input.txt').read().split('\n')
for inst in instructions:
    matches = re.findall('\d+|-\d+',inst)
    x,y,vx,vy = map(lambda x: int(x),matches)
    fx = (x + vx*seconds) % width
    fy = (y + vy*seconds) % height

    if 0 <= fx < mid_width and 0 <= fy < mid_height:
        q1 += 1
    elif mid_width < fx <= width and 0 <= fy < mid_height:
        q2 += 1
    elif 0 <= fx < mid_width and mid_height < fy <= height:
        q3 += 1
    elif mid_width < fx <= width and mid_height < fy <= height:
        q4 += 1
print(q1,q2,q3,q4)
print(q1*q2*q3*q4)