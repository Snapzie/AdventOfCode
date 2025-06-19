from hashlib import md5

code = []
for i in range(1,int(10e10)):
    hash = md5(bytes('ugkcyxxp'+str(i),'utf-8'))
    if str(hash.hexdigest())[:5] == '00000':
        print(hash.hexdigest(),hash.hexdigest()[5])
        code.append(hash.hexdigest()[5])
        if len(code) == 8:
            break
print(code)