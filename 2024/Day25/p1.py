blueprints = [[[1 if c == '#' else 0 for c in s] for s in l.split('\n')] for l in open('input.txt').read().split('\n\n')]

keys = []
locks = []
for blueprint in blueprints:
    pins = []
    for i in range(len(blueprint[0])):
        pins.append(sum([x[i] for x in blueprint])-1)
    if sum(blueprint[0]) == 5:
        locks.append(pins)
    else:
        keys.append(pins)

res = 0
for key in keys:
    for lock in locks:
        res += 1
        for pin in range(len(key)):
            if key[pin] + lock[pin] >= 6:
                res -= 1
                break
print(res)
        