instructions = list(map(int,open('input.txt').read().split(',')))

pointer = 0
A = 190384113204239
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

while pointer < len(instructions)-1:
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

print(','.join(out))