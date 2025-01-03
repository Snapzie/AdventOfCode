import re
from sympy import symbols, Eq, solve

equations = open('input.txt').read().split('\n\n')

tokens = 0
for eq in equations:
    instructions = eq.split('\n')
    matches = re.findall('\d+',instructions[0])
    x1,y1 = map(int,matches)

    matches = re.findall('\d+',instructions[1])
    x2,y2 = map(int,matches)

    matches = re.findall('\d+',instructions[2])
    X,Y = map(lambda x: int(x) + 10000000000000,matches)

    a,b = symbols('a b')
    e1 = Eq(x1*a + x2*b,X)
    e2 = Eq(y1*a + y2*b,Y)
    result = solve((e1,e2),(a,b))

    if result[a].is_integer and result[b].is_integer:
        tokens += result[a]*3 + result[b]
print(tokens)