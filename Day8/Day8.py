# Part 1
from collections import defaultdict
f = open('input.txt','r').read().strip()
inst, rest = f.split('\n\n')
d = defaultdict(int)

lines = rest.split('\n')
for line in lines:
    key,vals = line.split(' = ')
    d[key] = {'L': vals[1:4],'R': vals[6:9]}

idx = 0
counter = 0
step = 'AAA'
while(True):
    counter += 1
    step = d[step][inst[idx]]
    if step == 'ZZZ':
        break
    idx += 1
    idx = idx % len(inst)
print(counter)

# Part 2
from collections import defaultdict
import math
f = open('input.txt','r').read().strip()
inst, rest = f.split('\n\n')
d = defaultdict(int)

lines = rest.split('\n')
for line in lines:
    key,vals = line.split(' = ')
    d[key] = {'L': vals[1:4],'R': vals[6:9]}

steps = []
for k in d:
    if k[2] == 'A':
        steps.append(k)
print(steps)

idx = 0
counter = 0
loops = []
for step in steps:
    idx = 0
    counter = 0
    while(True):
        counter += 1
        step = d[step][inst[idx]]
        if step[2] == 'Z':
            loops.append(counter)
            break
        idx += 1
        idx = idx % len(inst)
print(loops)
print(math.lcm(*loops))