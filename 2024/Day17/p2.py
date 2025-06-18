seq = [0,3,5,5,7,1,7,4,3,0,5,7,2,1,4,2]

def recurse(seq,A=0):
    if len(seq) == 0:
        return A
    search = seq.pop(0)
    for i in range(8):
        A_i = (A << 3) | i
        # B = (((A_i % 8) ^ 2) ^ (A_i // 2**((A_i % 8) ^ 2))) ^ 7
        B = (A_i % 8) ^ (A_i >> ((A_i % 8) ^ 2)) ^ 5
        if B%8 == search:
            result = recurse(seq,A_i)
            if result:
                return result
    return None

print(recurse(seq))