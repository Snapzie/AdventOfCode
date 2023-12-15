f = open('./input.txt','r').read().strip()
lines = f.split(',')

res = []
for line in lines:
    curr = 0
    for c in line:
        curr += ord(c)
        curr *= 17
        curr = curr % 256
    res.append(curr)
print(sum(res))