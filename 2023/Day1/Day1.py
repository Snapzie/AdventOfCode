import re

# Part 1
calVals = []
with open('./input.csv','r') as f:
    for line in f:
        matches = re.findall(r'\d',line)
        val = int(''.join([matches[0],matches[-1]]))
        calVals.append(val)
print(sum(calVals))

# Part 2
def txt2Num(word):
    if len(word) > 1:
        if word == 'one':
            return '1'
        elif word == 'two':
            return '2'
        elif word == 'three':
            return '3'
        elif word == 'four':
            return '4'
        elif word == 'five':
            return '5'
        elif word == 'six':
            return '6'
        elif word == 'seven':
            return '7'
        elif word == 'eight':
            return '8'
        elif word == 'nine':
            return '9'
    else:
        return word

calVals = []
with open('./input2.csv','r') as f:
    for line in f:
        print(line)
        matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))',line)
        matches = [match.group(1) for match in matches]
        print(matches)
        matches = list(map(txt2Num,matches))
        print(matches)
        val = int(''.join([matches[0],matches[-1]]))
        calVals.append(val)
print(sum(calVals))