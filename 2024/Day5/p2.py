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

def sort_top(n):
    if n in perm_mark:
        return
    if n in tmp_mark:
        print(f"Error {n} in tmp")
        exit(0)
    tmp_mark.add(n)
    for m in rules[n]:
        if m not in seq:
            continue
        sort_top(m)
    perm_mark.add(n)
    L.append(n)

res = 0
for seq in seqs:
    valid = check_valid(seq)
    if not valid:
        L = []
        tmp_mark = set()
        perm_mark = set()

        while len(perm_mark) != len(seq):
            for val in seq:
                if val not in tmp_mark and val not in perm_mark:
                    sort_top(val)
        L = L[::-1]
        res += L[len(L)//2]
print(res)
