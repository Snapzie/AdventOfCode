from collections import defaultdict

rules, seqs = open('./input.txt').read().split('\n\n')
seqs = [[int(v) for v in l.split(',')] for l in seqs.split('\n')]
rules_list = [[int(k),int(v)] for (k,v) in [l.split('|') for l in rules.split('\n')]]
rules = defaultdict(lambda: [1],{k:[] for k in [l[0] for l in rules_list]})
# rules = {k:[] for k in [l[0] for l in rules_list]}
for l in rules_list:
    k = l[0]
    v = l[1]
    rules[k].append(v)

def check_valid(seq):
    for i,v in enumerate(seq):
        if i == 0: continue
        n_seq = seq[:i]
        valid = True if sum([1 if rv in n_seq else 0 for rv in rules[v]]) == 0 else False
        if not valid:
            return False
    return True

res = 0
for seq in seqs:
    valid = check_valid(seq)
    if valid:
        res += seq[len(seq)//2]
print(res)
