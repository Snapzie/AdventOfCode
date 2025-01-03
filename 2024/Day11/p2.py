from collections import defaultdict

stones = {int(k):1 for k in open('input.txt').read().split()}

for _ in range(75):
    new_stones = defaultdict(int)
    for stone,n in stones.items():
        if stone == 0:
            new_stones[1] += n
        elif len(str(stone)) % 2 == 0:
            string_stone = str(stone)
            left = int(string_stone[:len(string_stone)//2])
            right = int(string_stone[len(string_stone)//2:])
            new_stones[left] += n
            new_stones[right] += n
        else:
            new_stones[stone*2024] += n
    stones = new_stones

res = 0
for stone,n in stones.items():
    res += n
print(res)