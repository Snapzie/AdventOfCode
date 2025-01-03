# 174588 - high
# 172712 - high

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

def calc_seq(new_seq):
    for _ in range(25):
        seq = new_seq
        new_seq = [] 
        px,py = dir_pad['A']
        for inst in seq:
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
            if iy == 1 and px == 0:
                new_seq = new_seq + y_seq + x_seq
            else:
                new_seq = new_seq + x_seq + y_seq
            new_seq.append('A')
            px = ix
            py = iy
    return new_seq

complexity = []
sequences = [[c for c in l] for l in open('input.txt').read().split('\n')]
n_robots = 2
for org_seq in sequences:
    print(org_seq)
    new_seq = []
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
            # new_seq = new_seq + y_seq + x_seq
            new_seq = new_seq + calc_seq(y_seq + x_seq + ['A'])
        elif iy == 3 and px == 0:
            # new_seq = new_seq + x_seq + y_seq
            new_seq = new_seq + calc_seq(x_seq + y_seq + ['A'])
        else:
            # new_seq = new_seq + y_seq + x_seq
            # new_seq = new_seq + x_seq + y_seq
            s1 = calc_seq(y_seq + x_seq + ['A'])
            s2 = calc_seq(x_seq + y_seq + ['A'])
            if len(s1) < len(s2):
                new_seq = new_seq + s1
            else:
                new_seq = new_seq + s2
        # new_seq.append('A')
        print(new_seq)
        px = ix
        py = iy
    # print(''.join(new_seq))
    # for _ in range(n_robots):
    #     seq = new_seq
    #     # seq = ['v', '<', '<', 'A', '>', '>', '^', 'A', '<', 'A', '>', 'A', 'v', 'A', '<', '^', 'A', 'A', '>', 'A', '<', 'v', 'A', 'A', 'A', '>', '^', 'A']
    #     new_seq = [] 
    #     px,py = dir_pad['A']
    #     for inst in seq:
    #         ix,iy = dir_pad[inst]
    #         num_x = ix-px
    #         num_y = iy-py
    #         x_seq = []
    #         y_seq = []
    #         for _ in range(abs(num_y)):
    #             if num_y < 0:
    #                 y_seq.append('^')
    #             else:
    #                 y_seq.append('v')
    #         for _ in range(abs(num_x)):
    #             if num_x < 0:
    #                 x_seq.append('<')
    #             else:
    #                 x_seq.append('>')
    #         if py == 0:
    #             new_seq = new_seq + y_seq + x_seq
    #         else:
    #             new_seq = new_seq + x_seq + y_seq
    #         new_seq.append('A')
    #         px = ix
    #         py = iy
    #     print(''.join(new_seq))
    print(len(new_seq))
    # print(len(new_seq) * int(''.join(org_seq[:-1])))
    complexity.append(len(new_seq) * int(''.join(org_seq[:-1])))

print(sum(complexity))
# print(new_seq)