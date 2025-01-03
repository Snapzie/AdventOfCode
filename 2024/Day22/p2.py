secrets = list(map(int,open('input.txt').read().split('\n')))

banana_dict = {}

for i,secret in enumerate(secrets):
    seq = ''
    n = secret
    diffs = []
    for j in range(2000):
        seq += str(n)[-1]
        if j > 0:
            diffs.append(str(int(seq[j])-int(seq[j-1])))
        if j >= 4:
            search = ''.join(diffs[j-4:j])
            if not (i,search) in banana_dict:
                banana_dict[(i,search)] = int(seq[j])
        step1 = (n ^ (n * 64)) % 16777216
        step2 = (step1 ^ (step1 // 32)) % 16777216
        step3 = (step2 ^ (step2 * 2048)) % 16777216
        n = step3


res = 0
cache = {}
for i in range(-9,10):
    for j in range(-9,10):
        for k in range(-9,10):
            for l in range(-9,10):
                search = [i,j,k,l]
                if sum(search) > 0:
                    bananas = 0
                    search_string = ''.join(list(map(str,search)))
                    for monkey in range(len(secrets)):
                        if (monkey,search_string) in banana_dict:
                            bananas += banana_dict[(monkey,search_string)]
                    if bananas > res:
                        # print(f'{i}{j}{k}{l}: {bananas}')
                        res = bananas
print(res)