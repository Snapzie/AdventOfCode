import re

calVals = []
with open('./input.csv','r') as f:
    for line in f:
        matches = re.findall(r'\d',line)
        val = int(''.join([matches[0],matches[-1]]))
        calVals.append(val)
print(sum(calVals))