from collections import defaultdict
f = open('./input3.txt','r').read().strip()

class message():
    def __init__(self,msg_to,msg_from,signal):
        self.msg_to = msg_to
        self.msg_from = msg_from
        self.signal = signal

class counter():
    def __init__(self):
        self.low = 0
        self.high = 0
    def update(self,signal):
        if signal == 1:
            self.high += 1
        if signal == 0:
            self.low += 1

class broadcaster():
    def __repr__(self):
        return 'Broadcaster'
    def __init__(self,name,l,q,counter):
        self.name = name
        self.q = q
        self.broadcastTo = l
        self.counter = counter
    def process(self,msg):
        self.send(msg.signal)
        return
    def send(self,signal):
        for machine in self.broadcastTo:
            # print(f'From: {self.name}, To: {machine}, signal: {signal}')
            self.q.append(message(machine,self.name,signal))
            self.counter.update(signal)

class flipflop():
    def __repr__(self):
        return 'Flip-Flop'
    def __init__(self,name,l,q,counter):
        self.name = name
        self.broadcastTo = l
        self.q = q
        self.state = 0
        self.counter = counter
    def process(self,msg):
        if msg.signal == 1:
            return
        broadcastSignal = 1 if self.state == 0 else 0
        self.send(broadcastSignal)
        self.state = 0 if self.state == 1 else 1
        return
    def send(self,signal):
        for machine in self.broadcastTo:
            # print(f'From: {self.name}, To: {machine}, signal: {signal}')
            self.q.append(message(machine,self.name,signal))
            self.counter.update(signal)

class conjunction():
    def __repr__(self):
        return 'Conjunction'
    def __init__(self,name,l,q,counter):
        self.name = name
        self.q = q
        self.broadcastTo = l
        self.refs = []
        self.counter = counter
    def process(self,msg):
        for i,(machineName,_) in enumerate(self.refs):
            if machineName == msg.msg_from:
                self.refs[i][1] = msg.signal
                break
        if all([s == 1 for _,s in self.refs]):
            self.send(0)
        else:
            self.send(1)
        return
    def send(self,signal):
        for machine in self.broadcastTo:
            # print(f'From: {self.name}, To: {machine}, signal: {signal}')
            self.q.append(message(machine,self.name,signal))
            self.counter.update(signal)
# Parsing
d = defaultdict(lambda: False)
rows = list(map(lambda x: (x[0],x[1].split(', ')), [line.split(' -> ') for line in  f.split('\n')]))
print(rows)

## initialization
q = []
c = counter()
# machines
conjunctions = []
for name,l in rows:
    if name == 'broadcaster':
        d[name] = broadcaster(name,l,q,c)
    elif name[0] == '%':
        d[name[1:]] = flipflop(name[1:],l,q,c)
    elif name[0] == '&':
        d[name[1:]] = conjunction(name[1:],l,q,c)
        conjunctions.append((name[1:],d[name[1:]]))
    else:
        print('Unknown machine encountered')
# Refs for conjunctions
for conName,con in conjunctions:
    for name,l in rows:
        if conName in l:
            con.refs.append([name[1:],0])

print(d['cs'].refs)

# main loop
for i in range(1000000): # LCM solution computed by hand - part 2
    c.update(0)
    q.append(message('broadcaster','',0))
    while len(q) > 0:
        msg = q.pop(0)

        #### part 2 ####
        if msg.msg_from == 'hn' and msg.signal == 1:
            print(i)
        #### ###### ####
            
        if d[msg.msg_to] == False:
            continue
        d[msg.msg_to].process(msg)

    # print(d['cs'].refs) # kh, lz, tg, hn - part 2
print(c.low,c.high)