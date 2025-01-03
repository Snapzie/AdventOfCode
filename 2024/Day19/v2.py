# 397 - high
# 205 - low

patterns, designs = open('./input.txt').read().split('\n\n')
patterns = patterns.split(', ')
designs = designs.split('\n')

# def check_design(design):
#     # print(design,index)
#     if len(design) == 0:
#         return True
#     if design in cache:
#         return cache[design]
    
#     result = False
#     for pattern in patterns:
#         p_len = len(pattern)
#         if p_len > len(design):
#             continue
#         match = design[:p_len]
#         if pattern == match:
#             result = result or check_design(design[p_len:])
#             cache[design[p_len:]] = result
#     return result

# def check_design(design):
#     # print(design,index)
#     if len(design) == 0:
#         return []
#     if design in cache:
#         return cache[design]
    
#     # result = False
#     for pattern in patterns:
#         p_len = len(pattern)
#         if p_len > len(design):
#             continue
#         match = design[:p_len]
#         if pattern == match:
#             # print(f'pattern: {pattern}, match: {match}')
#             result = [pattern] + check_design(design[p_len:])
#             # print(f'result: {"".join(result)}')
#             cache[design[p_len:]] = result
#             return result
#     return ['-1']

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
    # print(design)
    # print(check_design(design))
    if check_design(design) is not None:
        res += 1
print(res)
