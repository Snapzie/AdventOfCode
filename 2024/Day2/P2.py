reports = [[int(num) for num in line.split()] for line in open('input.txt').read().split('\n')]

safe = 0
for report in reports:
    l1 = report[:-1]
    l2 = report[1:]
    diff = [e1-e2 for e1,e2 in zip(l1,l2)]
    if (all(e > 0 for e in diff) or all(e < 0 for e in diff)) and all( 1<=abs(e)<=3 for e in diff):
        safe += 1
        continue
    else:
        for i in range(len(report)):
            r = report[:i] + report[i+1:]
            l1 = r[:-1]
            l2 = r[1:]
            diff = [e1-e2 for e1,e2 in zip(l1,l2)]
            if (all(e > 0 for e in diff) or all(e < 0 for e in diff)) and all( 1<=abs(e)<=3 for e in diff):
                safe += 1
                break
print(safe)