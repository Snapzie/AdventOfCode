inputs = [list(map(lambda x: int(x),filter(lambda x: x != '',s.split(' ')))) for s in open('./input.txt').read().split('\n')]
transpose = [item for tuples in list(zip(*inputs)) for item in zip(*[iter(tuples)]*3)]

counter = 0
for a,b,c in transpose:
    if all(map(lambda sum,res: sum > res,*zip(*[(a+b,c),(a+c,b),(b+c,a)]))):
        counter += 1
print(counter)