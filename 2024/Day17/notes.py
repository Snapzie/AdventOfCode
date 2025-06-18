# larger tahn 630000000 
# A_org = 630000000
A_org = 281474976700656
while True:
    res = [(((((A_org // 8**i) % 8) ^ 2) ^ ((A_org // 8**i) // 2**(((A_org // 8**i) % 8) ^ 2))) ^ 7) % 8 for i in range(16)]
    if res == [2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0]:
        print(A_org)
        break
    A_org += 1
    if A_org % 10e6 == 0:
        print(A_org)
        
B = (((A % 8) ^ 2) ^ (A // 2**((A % 8) ^ 2))) ^ 7

C = A // 2**((A % 8) ^ 2)

A = A // 8


A = 10

011 100 101 011 000 000
