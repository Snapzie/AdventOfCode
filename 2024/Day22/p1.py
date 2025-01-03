secrets = list(map(int,open('input.txt').read().split('\n')))

res = 0
for secret in secrets:
    n = secret
    for _ in range(2000):
        step1 = (n ^ (n * 64)) % 16777216
        step2 = (step1 ^ (step1 // 32)) % 16777216
        step3 = (step2 ^ (step2 * 2048)) % 16777216
        n = step3
    res += n
print(res)