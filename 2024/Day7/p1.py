file = open('./input.txt').readlines()

res = 0
for line in file:
    target,numbers = line.split(': ')
    target = int(target)
    inputs = list(map(int,numbers.split()))
    output = []

    while inputs:
        input = inputs.pop(0)
        
        if len(output) == 0:
            output.append(input)
            continue

        new_output = []
        for out in output: 
            # if out*input <= target:
            new_output.append(out*input)
            # if out+input <= target:
            new_output.append(out+input)
            # if int(str(out) + str(input)) <= target:
            new_output.append(int(str(out) + str(input)))

        output = new_output

    if target in output:
        res += target

print(res)