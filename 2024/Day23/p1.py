connections = {}
for l in open('input.txt').read().split('\n'):
    k,v = l.split('-')
    if k in connections:
        connections[k].append(v)
    else:
        connections[k] = [v]
    v,k = l.split('-')
    if k in connections:
        connections[k].append(v)
    else:
        connections[k] = [v]

connected = set()
for conn1,conn1_vals in connections.items():
    for conn2 in conn1_vals:
        for conn3 in connections[conn2]:
            if conn3 in conn1_vals:
                tmp = [conn1,conn2,conn3]
                if conn1[0] == 't' or conn2[0] == 't' or conn3[0] == 't':
                    tmp.sort()
                    connected.add((tmp[0],tmp[1],tmp[2]))
connected = list(connected)
connected.sort()
print(len(connected))