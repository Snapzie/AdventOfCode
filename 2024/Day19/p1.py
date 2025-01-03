patterns, designs = open('./input.txt').read().split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')

def check_design(design,current=""):
    # print(len(design))
    if len(design) == 0:
        return current
    
    if design in cache:
        return cache[design]

    for pattern in patterns:
        p_len = len(pattern)
        # if p_len > len(design):
            # continue
        match = design[:p_len]
        if match == pattern:
            result = check_design(design[p_len:],current=current+pattern)
            cache[design[p_len:]] = result
            if result:
                return result
    return None

cache = {}
res = 0
for design in designs:
    if check_design(design) is not None:
        res += 1
print(res)