# Part 1
f = open('./input2.txt','r').read().strip()
lines = list(map(lambda x: (x[0],[int(e) for e in x[1].split(',')]),[line.split() for line in f.split('\n')]))

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
for input,inst in lines:
    perms = makePermutations(input)
    computes = doesCompute(inst,perms)
    res += sum(computes)
print(res)


