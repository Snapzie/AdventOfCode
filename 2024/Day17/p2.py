# 178229 - low

instructions = list(map(int,open('input.txt').read().split(',')))

seq = list(map(int,'2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0'.split(',')))
A_counter = 0

while True:
    pointer = 0
    A = A_counter
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
    seq_pointer = 0
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
            val = combo[operand] % 8
            if seq_pointer < len(seq) and seq[seq_pointer] == val:
                out.append(str(val))
                seq_pointer += 1
            else:
                break
        elif opcode == 6:
            B = A // 2**combo[operand]
            combo[5] = B
        elif opcode == 7:
            C = A // 2**combo[operand]
            combo[6] = C

        pointer += 2

    if ','.join(out) == '2,4,1,2,7,5,0,3,4,7,1,7,5,5,3,0':
        print(A_counter)
        print('Done')
        break
    
    A_counter += 1