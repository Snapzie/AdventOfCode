import re
from collections import Counter

inputs = open('./input.txt').read().split('\n')
sum = 0
for string in inputs:
    match = re.match(r'([A-Za-z-]+)-(\d{3})\[([A-Za-z]{5})\]',string)
    s,r_id,order = match.groups()
    dict = Counter(s)
    del dict['-']
    res = ''.join([x[0] for x in sorted(dict.items(),key=lambda x: (-x[1],x[0]))[:5]])
    if res == order:
        sum += int(r_id)
print(sum)