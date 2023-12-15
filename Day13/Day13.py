import numpy as np
# Part 1
# f = open('./input2.txt').read().strip()
# patterns = f.split('\n\n')
# # arr = np.array([[c for c in lines] for lines in f.split('\n\n')])
# patterns = np.array([np.array([[c for c in line] for line in lines.split('\n')]) for lines in f.split('\n\n')])
# # print(arr[0])

# res = 0
# for arr in patterns:
#     # Rows
#     for i in range(len(arr)-1):
#         if (arr[i] == arr[i+1]).all():
#             n = min(len(arr)-1-i,i+1)
#             a = arr[i+1-n:i+1]
#             b = arr[i+1:i+1+n]
#             # print(np.flip(a,axis=0))
#             # print(b)
#             if np.array_equal(np.flip(a,axis=0),b):
#                 # print(f'Horizontal: {i},{i+1}')
#                 res += (i+1)*100

#     # columns
#     for i in range(len(arr[0])-1):
#         if (arr[:,i] == arr[:,i+1]).all():
#             n = min(len(arr[0])-1-i,i+1)
#             a = arr[:,i+1-n:i+1]
#             b = arr[:,i+1:i+1+n]
#             if np.array_equal(np.flip(a,axis=1),b):
#                 # print(f'Vertical: {i},{i+1}')
#                 res += i+1
# print(res)

# Part 2
f = open('./input.txt').read().strip()
patterns = f.split('\n\n')
# arr = np.array([[c for c in lines] for lines in f.split('\n\n')])
patterns = np.array([np.array([[c for c in line] for line in lines.split('\n')]) for lines in f.split('\n\n')])
# print(arr[0])

res = 0
for arr in patterns:
    found = False
    # Rows
    for i in range(len(arr)-1):
        # print((arr[i] == arr[i+1]))
        if (len(arr[0]) - sum(arr[i] == arr[i+1])) < 2:
            n = min(len(arr)-1-i,i+1)
            a = arr[i+1-n:i+1]
            b = arr[i+1:i+1+n]
            # print(np.flip(a,axis=0))
            # print(b)
            truths = (np.flip(a,axis=0)==b)
            # print((truths.shape[0]*truths.shape[1]) - truths.sum())
            if (truths.shape[0]*truths.shape[1]) - truths.sum() == 1:
                # print(f'Horizontal: {i},{i+1}')
                res += (i+1)*100
                found = True
                break
    if found: continue
    # columns
    for i in range(len(arr[0])-1):
        if (len(arr) - sum(arr[:,i] == arr[:,i+1])) < 2:
            n = min(len(arr[0])-1-i,i+1)
            a = arr[:,i+1-n:i+1]
            b = arr[:,i+1:i+1+n]
            truths = (np.flip(a,axis=1)==b)
            # print((truths.shape[0]*truths.shape[1]) - truths.sum())
            if (truths.shape[0]*truths.shape[1]) - truths.sum() == 1:
                # print(f'Vertical: {i},{i+1}')
                res += i+1
                break
print(res)