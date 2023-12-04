res = 0
with open('./input.txt','r') as f:
    for line in f:
        winningList,nums = line.split(': ')[1].split(' | ')
        nums = [int(n) for n in nums.split()]
        winningList = [int(n) for n in winningList.split()]
        points = [n in winningList for n in nums]
        res += 0 if sum(points) == 0 else 2**(sum(points)-1)
print(res)

# Part 2
# winning = []
# own = []
# with open('./input.txt','r') as f:
#     for line in f:
#         winningList,nums = line.split(': ')[1].split(' | ')
#         nums = [int(n) for n in nums.split()]
#         winningList = [int(n) for n in winningList.split()]
#         own.append(nums)
#         winning.append(winningList)

# queue = list(range(0,len(winning)))
# res = len(queue)
# while len(queue) > 0:
#     points = sum([n in winning[queue[0]] for n in own[queue[0]]])
#     for i in range(1,points+1):
#         queue.append(queue[0]+i)
#     queue = queue[1:]
#     res += points
# print(res)

# Part 2.1
from collections import defaultdict

d = defaultdict(int)
with open('./input.txt','r') as f:
    for i,line in enumerate(f):
        winning,nums = line.split(': ')[1].split(' | ')
        nums = [int(n) for n in nums.split()]
        winning = [int(n) for n in winning.split()]

        d[str(i)] += 1
        points = sum([n in winning for n in nums])
        for j in range(1,points+1):
            d[str(i+j)] += d[str(i)]
res = sum(d.values())
print(res)