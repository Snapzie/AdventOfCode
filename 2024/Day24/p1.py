import re

wires,gates = open('input.txt').read().split('\n\n')

wire_dict = {}
for l in wires.split('\n'):
    wire,val = l.split(': ')
    wire_dict[wire] = int(val)

gates_dict = {}
for l in gates.split('\n'):
    instruction,wire = l.split(' -> ')
    gates_dict[wire] = instruction

def calc_wire(instruction,wire):
    if len(instruction.split(' XOR ')) == 2:
        left,right = instruction.split(' XOR ')
        left = wire_dict[left] if left in wire_dict else calc_wire(gates_dict[left],left)
        right = wire_dict[right] if right in wire_dict else calc_wire(gates_dict[right],right)
        wire_dict[wire] = left ^ right
        return wire_dict[wire]
    elif len(instruction.split(' OR ')) == 2:
        left,right = instruction.split(' OR ')
        left = wire_dict[left] if left in wire_dict else calc_wire(gates_dict[left],left)
        right = wire_dict[right] if right in wire_dict else calc_wire(gates_dict[right],right)
        wire_dict[wire] = left | right
        return wire_dict[wire]
    elif len(instruction.split(' AND ')) == 2:
        left,right = instruction.split(' AND ')
        left = wire_dict[left] if left in wire_dict else calc_wire(gates_dict[left],left)
        right = wire_dict[right] if right in wire_dict else calc_wire(gates_dict[right],right)
        wire_dict[wire] = left & right
        return wire_dict[wire]

for wire,instruction in gates_dict.items():
    if wire not in wire_dict:
        calc_wire(instruction,wire)

zs = []
for wire,val in wire_dict.items():
    if wire[0] == 'z':
        zs.append((wire,val))
zs.sort(key=lambda x: x[0])
print(int(''.join([str(val) for _,val in zs][::-1]),2))