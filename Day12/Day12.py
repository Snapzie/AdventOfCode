# Part 1
f = open('./input2.txt','r').read().strip()
lines = list(map(lambda x: (x[0],[int(e) for e in x[1].split(',')]),[line.split() for line in f.split('\n')]))

def doesCompute(input, inst):
    res = 0
    idx = 0
    popIdx = 0
    while idx < len(input):
        # print(idx,input,inst,popIdx,res)
        if input[idx] == '.':
            idx += 1
            continue
        if input[idx] == '#':
            if (idx-1 < 0 or input[idx-1] == '.') and all([e in ['#','?'] for e in input[idx:idx+inst[popIdx]]]):
                idx = idx+inst[popIdx]
                popIdx += 1
                continue
            else:
                return res
        if input[idx] == '?': # and popIdx < len(inst)-1
            if (idx-1 < 0 or input[idx-1] == '.'):# and (idx+1 > len(input) or input[idx+1] in ['.','?']): # then potential #
                if idx == len(input)-1 and popIdx < len(inst) and  inst[popIdx] == 1:
                    return res + 1
                if popIdx < len(inst):
                    if (inst[popIdx]+idx < len(input) and all([e in ['#','?'] for e in input[idx:idx+inst[popIdx]]]) and input[idx+inst[popIdx]] != '#'):
                        newInput = input[:idx] + '#' * max((inst[popIdx]),1) + input[idx+inst[popIdx]:]
                        # newInst = inst[1:]
                        # print(' ',  newInput,inst)
                        res += doesCompute(newInput,inst)
            input = input[:idx] + '.' + input[idx+1:]
        idx += 1
    if popIdx == len(inst):
        return res+1
    else:
        return res

for input,inst in lines:
    print(doesCompute(input,inst))