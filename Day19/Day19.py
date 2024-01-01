# # Part 1
# f = open('./input2.txt','r').read().strip()
# split = f.split('\n\n')
# workflowLines = split[0].split('\n')
# parts = split[1].split('\n')

# def workflow_to_dict(string):
#     tmp = string.split('{')
#     key = tmp[0]
#     val = tmp[1].strip('}')
#     conditions = val.split(',')
#     return key,conditions

# def str_to_dict(string):
#     string = string.strip('{}')
#     pairs = string.split(',')
#     return {key:int(value) for key,value in (pair.split('=') for pair in pairs)}

# workflows = {}
# for line in workflowLines:
#     key,conditions = workflow_to_dict(line)
#     workflows[key] = conditions
# parts = {k:str_to_dict(v) for k,v in enumerate(parts)}

# res_idx = []
# wf = 'in'
# for key, pdict in parts.items():
#     while wf != 'R' and wf != 'A':
#         for i,cond in enumerate(workflows[wf]):
#             if i == len(workflows[wf]) - 1:
#                 wf = cond
#                 break
#             c,res = cond.split(':')
#             p = c[0]
#             test = str(pdict[p]) + c[1:]
#             if eval(test):
#                 wf = res
#                 break
#     if wf == 'A':
#         res_idx.append(key)
#     wf = 'in'
# # print(res_idx)

# res = 0
# for idx in res_idx:
#     res += sum(parts[idx].values())
# print(res)


# Part 2
f = open('./input2.txt','r').read().strip()
split = f.split('\n\n')
workflowLines = split[0].split('\n')
parts = split[1].split('\n')

def workflow_to_dict(string):
    tmp = string.split('{')
    key = tmp[0]
    val = tmp[1].strip('}')
    conditions = val.split(',')
    return key,conditions

def str_to_dict(string):
    string = string.strip('{}')
    pairs = string.split(',')
    return {key:int(value) for key,value in (pair.split('=') for pair in pairs)}

workflows = {}
for line in workflowLines:
    key,conditions = workflow_to_dict(line)
    workflows[key] = conditions
parts = {k:str_to_dict(v) for k,v in enumerate(parts)}

def decent(wf,val_dict):
    if wf == 'R':
        # print(f'val: {val_dict}')
        # print(f'R')
        return 0
    if wf == 'A':
        # calc combs
        x = val_dict['x_max'] - val_dict['x_min'] + 1
        m = val_dict['m_max'] - val_dict['m_min'] + 1
        a = val_dict['a_max'] - val_dict['a_min'] + 1
        s = val_dict['s_max'] - val_dict['s_min'] + 1
        # print(f'val: {val_dict}')
        # print(f'A: {x*m*a*s}')
        return x*m*a*s
    
    out = 0
    for i,cond in enumerate(workflows[wf]):
        if i == len(workflows[wf]) - 1:
            # print(f'in: {cond}')
            out += decent(cond,val_dict)
            # print(f'out: {cond}')
            break
        # updates
        n_dict = dict(val_dict)
        c,res = cond.split(':')
        if c[1] == '>':
            val = int(c.split('>')[1])
            if c[0] == 'x':
                n_dict['x_min'] = val+1
                val_dict['x_max'] = val
            if c[0] == 'm':
                n_dict['m_min'] = val+1
                val_dict['m_max'] = val
            if c[0] == 'a':
                n_dict['a_min'] = val+1
                val_dict['a_max'] = val
            if c[0] == 's':
                n_dict['s_min'] = val+1
                val_dict['s_max'] = val
        if c[1] == '<':
            val = int(c.split('<')[1])
            if c[0] == 'x':
                n_dict['x_max'] = val-1
                val_dict['x_min'] = val
            if c[0] == 'm':
                n_dict['m_max'] = val-1
                val_dict['m_min'] = val
            if c[0] == 'a':
                n_dict['a_max'] = val-1
                val_dict['a_min'] = val
            if c[0] == 's':
                n_dict['s_max'] = val-1
                val_dict['s_min'] = val
        # print(f'val: {n_dict}')
        # print(f'in: {res}')
        out += decent(res,n_dict)
        # print(f'out: {res}') 
    return out

val_dict = {'x_min':1,'x_max':4000,'m_min':1,'m_max':4000,'a_min':1,'a_max':4000,'s_min':1,'s_max':4000}
print(decent('in',val_dict))

# 1  66 735 894 440 220
# 1  67 133 677 115 768
# 1  67 409 079 868 000


# res_idx = []
# wf = 'in'
# for cond in workflows['in']:
#     while wf != 'R' and wf != 'A':
#         for i,cond in enumerate(workflows[wf]):
#             if i == len(workflows[wf]) - 1:
#                 wf = cond
#                 break
#             c,res = cond.split(':')
#             # update
#             wf = res
#     break
# # print(res_idx)

# res = 0
# for idx in res_idx:
#     res += sum(parts[idx].values())
# print(res)

# px s_max = 1350 -> A a_min = 2006, m_min = 2091                                         == 1350 * 1994 * 1908 * 4000 V
# px s_max = 1350 -> qkq a_max = 2005 -> A x_max 1415                                     == 1350 * 2005 * 1415 * 4000 V
# px s_max = 1350 -> qkq a_max = 2005 -> crn x_min = 1416 -> A x_min = 2663               == 1350 * 2005 * 1337 * 4000 V
# px s_max = 1350 -> rfg a_min = 2006, m_max = 2090 -> A s_min = 537, x_max = 2440        ==  813 * 1994 * 2090 * 2440 V
# qqz s_min = 1351 -> qs s_min = 2771 -> A s_min = 3449                                   == 1229 * 4000 * 4000 * 4000 V
# qqz s_min = 1351 -> qs s_min = 2771 -> lnx s_max = 3448 -> A m_min = 1549                                            V
# qqz s_min = 1351 -> qs s_min = 2771 -> lnx s_max = 3448 -> A m_max = 1548                                            V
# qqz s_min = 1351 -> hdj s_max = 2770, m_max = 1800 -> A m_min = 839                     == 1419 *  961 * 4000 * 4000 V
# qqz s_min = 1351 -> hdj s_max = 2770, m_max = 1800 -> pv m_max = 838 -> A a_max 1716    == 1419 *  838 * 1716 * 4000 V