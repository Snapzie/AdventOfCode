patterns, designs = open('./input.txt').read().split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')

def check_design(design):
    # print(len(design))
    if len(design) == 0:
        return 1
    
    if design in cache:
        return cache[design]

    result = 0
    for pattern in patterns:
        p_len = len(pattern)
        # if p_len > len(design):
            # continue
        match = design[:p_len]
        if match == pattern:
            res = check_design(design[p_len:])
            cache[design[p_len:]] = res
            result += res
    return result

cache = {}
res = 0
for design in designs:
    res += check_design(design)
print(res)