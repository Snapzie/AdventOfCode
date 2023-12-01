import re

calVals = []
txt = '1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet'
txtList = txt.split('\n')
for line in txtList:
    matches = re.findall(r'\d',line)
    val = int(''.join([matches[0],matches[-1]]))
    calVals.append(val)
print(sum(calVals))