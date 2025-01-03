# 6377782328981 low

sequence = list(map(int,open('input.txt').read()))
vals = [[i,x] for i,x in enumerate(sequence[::2])]

checksum = 0
iteration = 0
i = 0
while len(vals) > 0:
    if i % 2 == 0:
        for j in range(sequence[i]):
            id,count = vals[0]
            if count < 0:
                iteration += -count
                vals = vals[1:]
                break
            # print(f'id: {id}, iter: {iteration}, sum: {id*iteration}')
            checksum += id*iteration
            # print(checksum)
            iteration += 1
            if count-1 == 0:
                if len(vals) == 1:
                    vals = []
                    break
                vals = vals[1:]     
            else:
                vals[0] = [id,count-1]

    else:
        space = sequence[i]
        considerations = 0
        while space > 0 and considerations != len(vals):
            considerations = 0
            for candiate in range(len(vals)-1,-1,-1):
                cid,cval = vals[candiate]
                if 0 < cval <= space:
                    skips = -cval
                    space -= cval
                    for _ in range(cval):
                        # print(f'cid: {cid}, iter: {iteration}, sum: {cid*iteration}')
                        checksum += cid*iteration
                        # print(checksum)
                        iteration += 1
                    vals[candiate] = [cid,skips]
                    break
                considerations += 1
            if considerations == len(vals):
                iteration += space
    i += 1
print(checksum)

