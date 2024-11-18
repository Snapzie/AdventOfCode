# Part 1
f = open('./input.txt','r').read().strip()

def diff(l):
    print(l)
    if sum(l) == 0:
        return l[0]
    else:
        diffs = list(map(lambda a,b: b-a,l[:-1],l[1:]))
        return diff(diffs)+l[-1]

res = 0
for line in f.split('\n'):
    nums = list(map(int,line.split()))
    res += diff(nums)
print(res)

# Part 2
f = open('./input.txt','r').read().strip()

def diff(l):
    print(l)
    if sum(l) == 0:
        return l[0]
    else:
        diffs = list(map(lambda a,b: b-a,l[:-1],l[1:]))
        return l[0]-diff(diffs)

res = 0
for line in f.split('\n'):
    nums = list(map(int,line.split()))
    res += diff(nums)
print(res)