instructions = list(map(int,open('input.txt').read().split(',')))
seq = instructions[::-1]

def do_instructions(A):
    pointer = 0
    B = 0
    C = 0

    combo = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: A,
    5: B,
    6: C
}
    out = []

    for _ in range(len(instructions)//2):
        opcode = instructions[pointer]
        operand = instructions[pointer+1]

        if opcode == 0:
            A = A // 2**combo[operand]
            combo[4] = A
        elif opcode == 1:
            B = B ^ operand
            combo[5] = B
        elif opcode == 2:
            B = combo[operand] % 8
            combo[5] = B
        elif opcode == 3:
            if A != 0:
                pointer = operand
                continue
        elif opcode == 4:
            B = B ^ C
            combo[5] = B
        elif opcode == 5:
            out.append(str(combo[operand] % 8))
        elif opcode == 6:
            B = A // 2**combo[operand]
            combo[5] = B
        elif opcode == 7:
            C = A // 2**combo[operand]
            combo[6] = C

        pointer += 2

    return int(''.join(out))

def recurse(seq,A=0):
    if len(seq) == 0:
        return A
    search = seq.pop(0)
    for i in range(8):
        A_i = (A << 3) | i
        output = do_instructions(A_i)
        if output%8 == search:
            result = recurse(seq,A_i)
            if result:
                return result
    return None

print(recurse(seq))