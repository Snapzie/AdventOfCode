# f = open('./input2.txt','r').read().strip()
# lines = list(map(lambda x: (x[0],[int(e) for e in x[1].split(',')]),[line.split() for line in f.split('\n')]))

# def doesCompute(input, inst):
#     res = 0
#     idx = 0
#     popIdx = 0
#     while idx < len(input):
#         # print(idx,input,inst,popIdx,res)
#         if input[idx] == '.':
#             idx += 1
#             continue
#         if input[idx] == '#':
#             if (idx-1 < 0 or input[idx-1] == '.') and all([e in ['#','?'] for e in input[idx:idx+inst[popIdx]]]):
#                 idx = idx+inst[popIdx]
#                 popIdx += 1
#                 continue
#             else:
#                 return res
#         if input[idx] == '?': # and popIdx < len(inst)-1
#             if (idx-1 < 0 or input[idx-1] == '.'):# and (idx+1 > len(input) or input[idx+1] in ['.','?']): # then potential #
#                 if idx == len(input)-1 and popIdx < len(inst) and  inst[popIdx] == 1:
#                     return res + 1
#                 if popIdx < len(inst):
#                     if (inst[popIdx]+idx < len(input) and all([e in ['#','?'] for e in input[idx:idx+inst[popIdx]]]) and input[idx+inst[popIdx]] != '#'):
#                         newInput = input[:idx] + '#' * max((inst[popIdx]),1) + input[idx+inst[popIdx]:]
#                         # newInst = inst[1:]
#                         # print(' ',  newInput,inst)
#                         res += doesCompute(newInput,inst)
#             input = input[:idx] + '.' + input[idx+1:]
#         idx += 1
#     if popIdx == len(inst):
#         return res+1
#     else:
#         return res

# Part 1
# def makePermutations(input):
#     permutations = []
#     if '?' in input:
#         return makePermutations(input.replace('?','.',1)) + makePermutations(input.replace('?','#',1))
#     else:
#         permutations.append(input)
#         return permutations

# def doesCompute(instOrg,permutations):
#     res = []
#     for input in permutations:
#         inst = [i for i in instOrg]
#         idx = 0
#         while idx < len(input):
#             if input[idx] == '.':
#                 idx += 1
#                 continue
#             if input[idx] == '#':
#                 if len(inst) > 0:
#                     instruction = inst.pop(0)
#                 else:
#                     res.append(False)
#                     break

#                 remaining = len(input) - idx
#                 if remaining < instruction:
#                     res.append(False)
#                     break
                
#                 if (idx-1 < 0 or input[idx-1] == '.') and all([e == '#' for e in input[idx:idx+instruction]]):
#                     idx = idx+instruction
#                     # continue
#                 else:
#                     res.append(False)
#                     break
#         else:
#             if len(inst) == 0: 
#                 res.append(True)
#             else:
#                 res.append(False)
#     return res

# res = 0
# for input,inst in lines:
#     perms = makePermutations(input)
#     computes = doesCompute(inst,perms)
#     res += sum(computes)
# print(res)


# Part 2
# import math
# import numpy as np
# f = open('./input2.txt','r').read().strip()
# lines = list(map(lambda x: [x[0],[int(e) for e in x[1].split(',')]],[line.split() for line in f.split('\n')]))

# # lines = [lines[-1]]
# print(lines)
# res = 0
# for i,(line,insts) in enumerate(lines,start=1):
#     # print(lline)
#     # line = lline[0]
#     # print(line)
#     # insts = lline[1]
#     inner_res = 0
#     insts_idx = 0
#     line_idx = 0
#     q_lim = len(line)
#     print(i)
#     while line_idx < len(line) and insts_idx < len(insts):
#         # print(line[line_idx],line_idx,insts_idx )
#         while line_idx < len(line) and line[line_idx] == '.':
#             line_idx += 1
#         if line_idx == len(line):
#             continue
#         if line[line_idx] == '#':
#             tmp_idx = line_idx + insts[insts_idx]
#             if tmp_idx >= len(line)-1:
#                 insts_idx += 1
#                 line_idx = tmp_idx+1
#                 continue
#             if line[tmp_idx] == '.' or line[tmp_idx] == '?':
#                 line_idx = tmp_idx+1
#                 insts_idx += 1
#                 continue
#             if line[tmp_idx] == '#':
#                 inner_res = 0
#                 insts_idx = 0
#                 line_idx = 0
#                 q_lim -= q_lim
#                 # line = line[::-1]
#                 # insts = insts[::-1]
#                 continue
#             # else -- should not happen?
#         if line[line_idx] == '?':
#             q_count = 1
#             while line_idx+q_count < len(line) and q_count < q_lim and line[line_idx+q_count] == '?':
#                 q_count += 1
#             # print(q_count)
#             inst_sum = insts[insts_idx]
#             if inst_sum < q_count:
#                 insts_count = 1
#                 while insts_idx+1 < len(insts) and inst_sum + insts[insts_idx+1] < q_count:
#                     inst_sum += insts[insts_idx+1]
#                     insts_idx += 1
#                     insts_count += 1
#                 n = q_count - (insts_count - 1) - (inst_sum - insts_count)
#                 inner_res += math.comb(n,insts_count)
                
#                 line_idx += q_count
#                 insts_idx += 1
#             else:
#                 tmp_idx = line_idx + insts[insts_idx]
#                 if tmp_idx >= len(line)-1:
#                     break
#                 if line[tmp_idx] == '#':
#                     line_idx += 1
#                 if line[tmp_idx] == '.' or line[tmp_idx] == '?':
#                     line_idx = tmp_idx+1
#                     insts_idx += 1
#     if inner_res == 0:
#         res += 1
#     else:
#         res += inner_res
# print(res)


f = open('./input2.txt','r').read().strip()
lines = list(map(lambda x: (x[0],[int(e) for e in x[1].split(',')]),[line.split() for line in f.split('\n')]))

# Part 1
def makePermutations(input):
    permutations = []
    if '?' in input:
        return makePermutations(input.replace('?','.',1)) + makePermutations(input.replace('?','#',1))
    else:
        permutations.append(input)
        return permutations

def doesCompute(instOrg,permutations):
    res = []
    for input in permutations:
        inst = [i for i in instOrg]
        idx = 0
        while idx < len(input):
            if input[idx] == '.':
                idx += 1
                continue
            if input[idx] == '#':
                if len(inst) > 0:
                    instruction = inst.pop(0)
                else:
                    res.append(False)
                    break

                remaining = len(input) - idx
                if remaining < instruction:
                    res.append(False)
                    break
                
                if (idx-1 < 0 or input[idx-1] == '.') and all([e == '#' for e in input[idx:idx+instruction]]):
                    idx = idx+instruction
                    # continue
                else:
                    res.append(False)
                    break
        else:
            if len(inst) == 0: 
                res.append(True)
            else:
                res.append(False)
    return res

res = 0
total = len(lines)
for i,(input,inst) in enumerate(lines):
    print(f'{i}/{total}')
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0

    perms = makePermutations(input)
    computes = doesCompute(inst,perms)
    res1 += sum(computes)
    # print(res1)

    if input[-1] == '#' or input[0] == '#':
        perms21 = makePermutations('.'+input)
        computes = doesCompute(inst,perms21)
        res += sum(computes)**4 * res1
    else:
        perms21 = makePermutations(input+'?')
        perms22 = makePermutations('?'+input)
        computes = max(doesCompute(inst,perms21),doesCompute(inst,perms22))
        res3 += sum(computes)**4 * res1

        perms23 = makePermutations('?'+input+'?')
        computes = doesCompute(inst,perms23)
        res4 += sum(computes)**2 * res1**3

        res += max(res2,res3)
print(res)


# 10116216700888 -- low
# 10343457217413 -- low
# 10800000000000 -- low

# ??????##??.#????? ? ??????##??.#????? ? ??????##??.#????? ? ??????##??.#????? ? ??????##??.#????? ? ??????##??.#????? 6,1,3
# ..######.#.###.## # ###.#.###..###### .
# ..######.#.###... . ..######