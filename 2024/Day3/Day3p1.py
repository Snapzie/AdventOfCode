
# def check_digit(idx):
#     if seq[i:i+3].isdigit():
#         print(seq[i:i+3])
#         return int(seq[i:i+3]), idx+3
#     elif seq[i:i+2].isdigit():
#         print(seq[i:i+2])
#         return int(seq[i:i+2]), idx+2
#     elif seq[i:i+1].isdigit():
#         print(seq[i:i+1])
#         return int(seq[i:i+1]), idx+1
#     else:
#         return '', idx+3

# seq = open('input.txt').read()
# print(seq)
# i = 0
# res = 0
# count = True
# while True:
#     if i > len(seq):
#         break
#     if 'mul(' == seq[i:i+4]:
#         print('mul(')
#         i += 4
#         num1,i = check_digit(i)
#         if num1 != '':
#             if seq[i] == ',':
#                 i += 1
#                 num2,i = check_digit(i)
#                 if num2 != '':
#                     if seq[i] == ')':
#                         if count:
#                             res += num1*num2
#     elif "don't" == seq[i:i+5]:
#         count = False
#         i += 5
#     elif "do" == seq[i:i+2]:
#         count = True
#         i += 2
#     else:
#         i += 1
# print(res)

import re
text = open('input.txt').read()
pattern = '(mul\(\d{1,3},\d{1,3}\))|(don\'t)|(do)'
matches = re.finditer(pattern,text)

res = 0
add = True
for m in matches:
    if m.group() == "don't":
        add = False
    elif m.group() == "do":
        add = True
    else:
        if add:
            vals = re.findall('\d{1,3}',m.group())
            res += int(vals[0]) * int(vals[1])
print(res)