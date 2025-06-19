wires,gates = open('input.txt').read().split('\n\n')

S_int = []
C_int = []
C_in = []
carry_and = []
C_out = []

for gate in gates.split('\n'):
    rest,result = gate.split(' -> ')
    left,operator,right = rest.split(' ')

    # if result.startswith('z'):
    #     if not operator == 'XOR':
    #         print(f'{left} {operator} {right} -> {result}')
    if ((left.startswith('x') and right.startswith('y')) or (left.startswith('y') and right.startswith('x'))) and operator == 'XOR':
        S_int.append(result)
    elif ((left.startswith('x') and right.startswith('y')) or (left.startswith('y') and right.startswith('x'))) and operator == 'AND':
        C_int.append(result)


for gate in gates.split('\n'):
    rest,result = gate.split(' -> ')
    left,operator,right = rest.split(' ')

    if result.startswith('z') and operator == 'XOR' and left in S_int:
        C_in.append(right)
    elif result.startswith('z') and operator == 'XOR' and right in S_int:
        C_in.append(left)



for gate in gates.split('\n'):
    rest,result = gate.split(' -> ')
    left,operator,right = rest.split(' ')

    if operator == 'AND' and left in S_int and right in C_in:
        carry_and.append(result)
    elif operator == 'AND' and left in C_in and right in S_int:
        carry_and.append(result)


for gate in gates.split('\n'):
    rest,result = gate.split(' -> ')
    left,operator,right = rest.split(' ')

    if operator == 'OR' and left in C_int and right in carry_and:
        C_out.append(result)
    elif operator == 'OR' and right in C_int and left in carry_and:
        C_out.append(result)


for gate in gates.split('\n'):
    rest,result = gate.split(' -> ')
    left,operator,right = rest.split(' ')

    if ((left.startswith('x') and right.startswith('y')) or (left.startswith('y') and right.startswith('x'))) and operator == 'XOR' and result in S_int:
        continue
    if ((left.startswith('x') and right.startswith('y')) or (left.startswith('y') and right.startswith('x'))) and operator == 'AND' and result in C_int:
        continue
    if left in S_int and right in C_in and operator == 'XOR' and result.startswith('z'):
        continue
    if right in S_int and left in C_in and operator == 'XOR' and result.startswith('z'):
        continue
    if left in S_int and right in C_in and result in carry_and and operator == 'AND':
        continue
    if right in S_int and left in C_in and result in carry_and and operator == 'AND':
        continue
    if operator == 'OR' and result in C_out and left in C_int and right in carry_and:
        continue
    if operator == 'OR' and result in C_out and right in C_int and left in carry_and:
        continue

    print(f'{left} {operator} {right} -> {result}')


'''
S_int = A XOR B
C_int = A AND B
S = S_int XOR C_in
C_out = C_int OR (S_int AND C_in)


fsf OR nqs -> z12
jfk AND vkb -> z29
x37 AND y37 -> z37
'''