import numpy as np
text = np.array([[s for s in l] for l in open('./input.txt').read().split('\n')])

res = 0
for j in range(len(text)):
    for i in range(len(text[0])):
        if text[j][i] == 'X':
            if i <= len(text[0])-4:
                if ''.join(text[j,i:i+4]) == 'XMAS': res += 1
            if i >= 3:
                if ''.join(text[j,i-3:i+1])[::-1] == 'XMAS': res += 1
            if j <= len(text)-4:
                if ''.join(text[j:j+4,i]) == 'XMAS': res += 1
            if j >= 3:
                if ''.join(text[j-3:j+1,i])[::-1] == 'XMAS': res += 1
            if i <= len(text[0])-4 and j >= 3:
                if text[j,i] + text[j-1,i+1] + text[j-2,i+2] + text[j-3,i+3] == 'XMAS': res += 1
            if i >= 3 and j >= 3:
                if text[j,i] + text[j-1,i-1] + text[j-2,i-2] + text[j-3,i-3] == 'XMAS': res += 1
            if i >= 3 and j <= len(text)-4:
                if text[j,i] + text[j+1,i-1] + text[j+2,i-2] + text[j+3,i-3] == 'XMAS': res += 1
            if i <= len(text[0])-4 and j <= len(text)-4:
                if text[j,i] + text[j+1,i+1] + text[j+2,i+2] + text[j+3,i+3] == 'XMAS': res += 1
print(res)


res = 0
for j in range(len(text)):
    for i in range(len(text[0])):
        if text[j][i] == 'A':
            if 1 <= i <= len(text[0])-2 and 1 <= j <= len(text)-2:
                if ((text[j-1,i+1] == 'M' and text[j+1,i-1] == 'S') or (text[j-1,i+1] == 'S' and text[j+1,i-1] == 'M')) and ((text[j-1,i-1] == 'M' and text[j+1,i+1] == 'S') or (text[j-1,i-1] == 'S' and text[j+1,i+1] == 'M')):
                    res+=1
            
print(res)