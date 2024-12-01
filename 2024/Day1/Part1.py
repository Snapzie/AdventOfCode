pairs = open('./input.txt').read().split('\n')
left_list = []
right_list = []
for i,(l,r) in enumerate(map(str.split,pairs)):
    left_list.append(int(l))
    right_list.append(int(r)) 
left_list.sort()
right_list.sort()

res = 0
for l,r in zip(left_list,right_list):
    res += abs(l-r)
print(res)