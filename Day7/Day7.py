from collections import defaultdict

fiveKind = []
fourKind = []
house = []
threeKind = []
twoPair = []
onePair = []
high = []
dict_ranking = {'2':0,'3':1,'4':2,'5':3,'6':4,'7':5,'8':6,'9':7,'T':8,'J':9,'Q':10,'K':11,'A':12}

f = open('./input.txt','r').read().strip()
for line in f.split('\n'):
    hand,bid = line.split()
    d = defaultdict(int)
    for c in hand:
        d[c] = d[c] + 1
    vals = sorted(list(d.values()))[::-1]
    if vals[0] == 5:
        fiveKind.append((hand,int(bid)))
    elif vals[0] == 4:
        fourKind.append((hand,int(bid)))
    elif vals[0] == 3 and vals[1] == 2:
        house.append((hand,int(bid)))
    elif vals[0] == 3:
        threeKind.append((hand,int(bid)))
    elif vals[0] == 2 and vals[1] == 2:
        twoPair.append((hand,int(bid)))
    elif vals[0] == 2:
        onePair.append((hand,int(bid)))
    else:
        high.append((hand,int(bid)))
l = [high,onePair,twoPair,threeKind,house,fourKind,fiveKind]
res = []
for li in l:
    s_list = sorted(li,key=lambda x: (dict_ranking[x[0][0]],dict_ranking[x[0][1]],dict_ranking[x[0][2]],dict_ranking[x[0][3]],dict_ranking[x[0][4]]))
    res = res+s_list
asw = 0
for i in range(len(res)):
    asw += res[i][1] * (i+1)
print(asw) 