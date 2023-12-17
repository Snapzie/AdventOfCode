# f = open('./input.txt','r').read().strip()
# lines = f.split(',')

# res = []
# for line in lines:
#     curr = 0
#     for c in line:
#         curr += ord(c)
#         curr *= 17
#         curr = curr % 256
#     res.append(curr)
# print(sum(res))

# part 2
f = open('./input.txt','r').read().strip()
lines = f.split(',')

def getBox(line):
    idx = 0
    curr = 0
    while line[idx] not in ['=','-']:
        curr += ord(line[idx])
        curr *= 17
        curr = curr % 256
        idx += 1
    return curr

boxes = [[] for _ in range(256)]
for line in lines:
    print(line)
    box = getBox(line)
    if '-' in line:
        label = line[:line.index('-')]
        l = boxes[box]
        for i in range(len(l)):
            print(i,l)
            if l[i][0] == label:
                l.pop(i)
                break
    if '=' in line:
        label = line[:line.index('=')]
        lens = line[line.index('=')+1:]
        l = boxes[box]
        for i in range(len(l)):
            if l[i][0] == label:
                l[i][1] = lens
                break
        else: boxes[box].append([label,lens])
print(boxes)

res = 0
for i,box in enumerate(boxes,start=1):
    for j,(_,lens) in enumerate(box,start=1):
        res += i * j * int(lens)
print(res)