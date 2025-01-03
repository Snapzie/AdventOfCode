sequence = list(map(int,open('input.txt').read()))
vals = [[i,x] for i,x in enumerate(sequence[::2])]

checksum = 0
iteration = 0
i = 0
while len(vals) > 0:
    idx = 0 if i % 2 == 0 else -1
    for j in range(sequence[i]):
        id,count = vals[idx]
        checksum += id*iteration
        iteration += 1
        if count-1 == 0:
            if len(vals) == 1:
                vals = []
                break
            vals = vals[1:] if i % 2 == 0 else vals[:-1]
        else:
            vals[idx] = [id,count-1]
    i += 1
print(checksum)