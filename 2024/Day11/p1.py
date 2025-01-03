org_stones = list(map(int,open('input.txt').read().split()))

res = 0
for org_stone in org_stones:
    stones = [org_stone]
    for _ in range(75):
        new_stones = []
        for i in range(len(stones)):
            if stones[i] == 0:
                new_stones.append(1)
            elif len(str(stones[i])) % 2 == 0:
                string_stone = str(stones[i])
                left = int(string_stone[:len(string_stone)//2])
                right = int(string_stone[len(string_stone)//2:])
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(stones[i]*2024)
        stones = new_stones
    res += len(stones)
print(res)



        