# Part 1
from functools import reduce
f = open('./input.txt','r').read().strip().split('\n')
time, distance = [list(map(int,x.split(':')[1].split())) for x in f]

res = []
for i in range(len(time)):
    asw = 0
    for j in range(1,time[i]+1):
        if (time[i]-j)*j > distance[i]:
            asw += 1
    res.append(asw)
print(reduce(lambda a,b: a*b,res))

# Part 2
from functools import reduce
f = open('./input.txt','r').read().strip().split('\n')
time, distance = [int(reduce(lambda a,b: a+b,x.split(':')[1].split())) for x in f]

asw = 0
for j in range(1,time+1):
    if (time-j)*j > distance:
        asw += 1
print(asw)