from collections import defaultdict

keys = ['Dest','Source','Range']
f = open('./input.txt').read().strip()
for line in f.split('\n\n'):
    if line.startswith('seeds:'):
        seeds = [int(x) for x in line.split(': ')[1].split()]
    if line.startswith('seed-to-soil'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        seed2Soil = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('soil-to-fertilizer'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        soil2fert = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('fertilizer-to-water'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        fert2water = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('water-to-light'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        water2light = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('light-to-temperature'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        light2temp = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('temperature-to-humidity'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        temp2humid = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('humidity-to-location'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        humid2dest = [{k:v for k,v in zip(keys,val)} for val in vals]

dests = []
for idx in seeds:
    for dict in seed2Soil:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in soil2fert:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in fert2water:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in water2light:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in light2temp:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in temp2humid:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break
    for dict in humid2dest:
        if dict['Source'] <= idx <= dict['Source']+dict['Range']:
            idx = idx + (dict['Dest'] - dict['Source'])
            break    
    dests.append(idx)
print(min(dests))


# Part 2
keys = ['Dest','Source','Range']
f = open('./input2.txt').read().strip()
for line in f.split('\n\n'):
    if line.startswith('seeds:'):
        seeds = [int(x) for x in line.split(': ')[1].split()]
        seedpairs = list(zip(seeds[::2],seeds[1::2]))
        print(seedpairs)
    if line.startswith('seed-to-soil'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        seed2Soil = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('soil-to-fertilizer'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        soil2fert = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('fertilizer-to-water'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        fert2water = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('water-to-light'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        water2light = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('light-to-temperature'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        light2temp = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('temperature-to-humidity'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        temp2humid = [{k:v for k,v in zip(keys,val)} for val in vals]
    if line.startswith('humidity-to-location'):
        vals = [[int(x) for x in val] for val in [x.split() for x in line.split('\n')[1:]]]
        humid2dest = [{k:v for k,v in zip(keys,val)} for val in vals]

dests = []
dicts = [humid2dest,temp2humid,light2temp,water2light,fert2water,soil2fert,seed2Soil]
found = True
count = 0
# for idx in range(0,100):
while found:
    idx = count
    for dictlist in dicts:
        for dict in dictlist:
            if dict['Dest'] <= idx <= dict['Dest']+dict['Range']:
                idx = idx + (dict['Source'] - dict['Dest'])
                break
    for seed_start, seed_end in seedpairs:
        if seed_start <= idx <= seed_start+seed_end:
            print(count)
            found = False
    count += 1