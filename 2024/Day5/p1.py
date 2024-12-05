from itertools import permutations

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
            return False,i
    return True,seq

def make_combs(seq,c):
    seqs = []
    for i in range(len(seq)+1):
        seqs.append(seq[:i]+[c]+seq[i:])
    return seqs

def make_combs2(seq):
    return permutations(seq)

res = []
for seq in seqs:
    valid, i = check_valid(seq)
    if not valid:
        print(seq)
        # c = seq[i]
        # n_seq = seq[:i]+seq[i+1:]
        # combs = make_combs(n_seq,c)
        combs = make_combs2(seq)
        # print(combs,c)
        # for c in combs: 
        for c in permutations(seq):
            valid2,_ = check_valid(c)
            if valid2:
                middle = c[len(c)//2]
                # print(middle)
                res.append(middle)
                break
print(sum(res))