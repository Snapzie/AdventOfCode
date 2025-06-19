from collections import defaultdict

num_pad = {
    '7': (0,0),
    '8': (1,0),
    '9': (2,0),
    '4': (0,1),
    '5': (1,1),
    '6': (2,1),
    '1': (0,2),
    '2': (1,2),
    '3': (2,2),
    '0': (1,3),
    'A': (2,3)
}

dir_pad = {
    '^': (1,0),
    'A': (2,0),
    '<': (0,1),
    'v': (1,1),
    '>': (2,1)
}

cache = {}

def calc_seq(new_seq):
    for _ in range(25):
        seq = new_seq.copy()
        new_seq = defaultdict(int) 
        px,py = dir_pad['A']
        for group,n in seq.items():
            for inst in group:
                ix,iy = dir_pad[inst]
                num_x = ix-px
                num_y = iy-py
                x_seq = []
                y_seq = []
                for _ in range(abs(num_y)):
                    if num_y < 0:
                        y_seq.append('^')
                    else:
                        y_seq.append('v')
                for _ in range(abs(num_x)):
                    if num_x < 0:
                        x_seq.append('<')
                    else:
                        x_seq.append('>')
                if iy == 0 and px == 0:
                    new_seq[''.join(x_seq + y_seq + ['A'])] += n
                elif ix == 0 and py == 0:
                    new_seq[''.join(y_seq + x_seq + ['A'])] += n
                elif num_x < 0:
                    new_seq[''.join(x_seq + y_seq + ['A'])] += n
                elif num_y != 0:
                    new_seq[''.join(y_seq + x_seq + ['A'])] += n
                else:
                    new_seq[''.join(x_seq + y_seq + ['A'])] += n
                px = ix
                py = iy
    return new_seq

complexity = []
sequences = [[c for c in l] for l in open('input.txt').read().split('\n')]
n_robots = 2
for org_seq in sequences:
    dict_seq = defaultdict(int)
    px,py = num_pad['A']
    for inst in org_seq:
        ix,iy = num_pad[inst]
        num_x = ix-px
        num_y = iy-py
        x_seq = []
        y_seq = []
        for _ in range(abs(num_y)):
            if num_y < 0:
                y_seq.append('^')
            else:
                y_seq.append('v')
        for _ in range(abs(num_x)):
            if num_x < 0:
                x_seq.append('<')
            else:
                x_seq.append('>')
        if py == 3 and ix == 0:
            dict_seq[''.join(y_seq + x_seq + ['A'])] += 1
        elif iy == 3 and px == 0:
            dict_seq[''.join(x_seq + y_seq + ['A'])] += 1
        elif num_x < 0:
            dict_seq[''.join(x_seq + y_seq + ['A'])] += 1
        elif num_y != 0:
            dict_seq[''.join(y_seq + x_seq + ['A'])] += 1
        else:
            dict_seq[''.join(x_seq + y_seq + ['A'])] += 1
        px = ix
        py = iy
    res_dict = calc_seq(dict_seq)
    dict_len = 0
    for k,v in res_dict.items():
        dict_len += len(k) * v
    complexity.append(dict_len * int(''.join(org_seq[:-1])))
print(sum(complexity))