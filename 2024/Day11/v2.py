stones = list(map(int,open('input.txt').read().split()))

def calc_stone(iteration,val):
    if iteration == 75:
        return 1
    
    if val == 0:
        return calc_stone(iteration+1,1)
    elif len(str(val)) % 2 == 0:
        string_stone = str(val)
        left = int(string_stone[:len(string_stone)//2])
        right = int(string_stone[len(string_stone)//2:])
        return calc_stone(iteration+1,left) + calc_stone(iteration+1,right)
    else:
        return calc_stone(iteration+1,val*2024)

res = 0
for stone in stones:
    res += calc_stone(0,stone)
print(res)


