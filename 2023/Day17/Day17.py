import numpy as np
from collections import Counter
from collections import defaultdict
# import fibheap as fib
import queue
f = open('./input2.txt','r').read().strip()
costMap = np.array([[int(c) for c in line] for line in f.split('\n')])
costMap = costMap / 2.5
print(costMap)

class node():
    def __init__(self,f,g,parrent,pos,dirs):
        self.f = f
        self.g = g
        self.parrent = parrent
        self.pos = pos
        self.dirs = dirs
    def __lt__(a,b):
        return min(a.f,b.f)

# openList = [node(0,0,None,(0,0),[None,None,None])]
openList = queue.PriorityQueue(0)
openList.put((0,node(0,0,None,(0,0),[None,None,None])))
# openList = fib.makefheap()
# fib.fheappush(openList,node(0,0,None,(0,0),[None,None,None]))

# closedList = []
closedList = defaultdict(lambda: -1)
found = False
endNode = None
D2 = np.sqrt(2)
goal = (len(costMap)-1,len(costMap[0])-1)
counter = 0
# while len(openList) > 0:
while openList.qsize() > 0:
    counter += 1
# while openList.num_nodes > 0:
    # q = min(openList,key=lambda x: x.f)
    q = openList.get()[1]
    # q = fib.fheappop(openList)
    # openList.remove(q)

    # If goal
    if q.pos == goal:
        endNode = q
        print(q.pos,q.f)
        break

    coords = [((0,1),'R'),((1,0),'D'),((0,-1),'L'),((-1,0),'U')] # R,D,L,U
    for (ry,rx),dir in coords:
        if (q.dirs[0] == dir and q.dirs[1] == dir and q.dirs[2] == dir):
            continue
        y,x = q.pos
        if y+ry < 0 or y+ry > len(costMap)-1 or x+rx < 0 or x+rx > len(costMap[0])-1:
            continue
        npos = (y+ry,x+rx)
        parrent = q
        penalty = 0
        # if (q.dirs[0] == dir and q.dirs[1] == dir and q.dirs[2] == dir) or (q.dirs[2] == 'L' and dir == 'R') or (q.dirs[2] == 'R' and dir == 'L') or (q.dirs[2] == 'D' and dir == 'U') or (q.dirs[2] == 'U' and dir == 'D'):
        #     penalty = 1e6
        g = q.g + costMap[npos[ 0],npos[1]] + penalty
        h = (abs(npos[0]-goal[0]) + abs(npos[1]-goal[1]))*2
        # dx = abs(npos[1] - goal[1])
        # dy = abs(npos[0] - goal[0])
        # h = 1 * (dx + dy) + (D2 - 2 * 1) * min(dx, dy)
        # h = np.sqrt(dx**2+dy**2)
        # print(g,h)
        f = g + h
        ndirs = list(q.dirs)
        ndirs.append(dir)
        ndirs.pop(0)

        skip = False
        # for n in openList:
        #     if n.pos == npos and n.f < f:# and len(Counter(ndirs)) == 1:
        #         skip = True
        # for n in closedList:
        #     if n.pos == npos and n.f < f:
        #         skip = True
        val = closedList[npos]
        if val != -1 and closedList[npos] < f:
            skip = True
        
        if not skip:
            # openList.append(node(f,g,q,npos,ndirs))
            openList.put((f,node(f,g,q,npos,ndirs)))
            # fib.fheappush(openList,node(f,g,q,npos,ndirs))
    
    # closedList.append(q)
    val = closedList[q.pos]
    if val == -1:
        closedList[q.pos] = q.f
    elif closedList[q.pos] < q.f:
        closedList[q.pos] = q.f

    # print(closedList)
    # if counter % 10000 == 0:
    if counter % 500000 == 0:
        # print(len(openList))
        print(openList.qsize())
        print('Printing')
        parr = np.full((141,141),0)
        for (y,x),val in closedList.items():
            parr[y,x] = val#str(val)

        with open('./out.txt','w') as f:
            for row in parr:
                for val in row:
                    # val = int(val)
                    f.write(f'{val:5.0f}')
                f.write('\n')

print('Printing')
parr = np.full((141,141),0)
for (y,x),val in closedList.items():
    parr[y,x] = val#str(val)

with open('./out.txt','w') as f:
    for row in parr:
        for val in row:
            # val = int(val)
            f.write(f'{val:5.0f}')
        f.write('\n')
    
# for n in closedList:
#     print(n.f,n.pos)
# while endNode.parrent is not None:
#     print(endNode.pos,endNode.f,endNode.dirs)
#     endNode = endNode.parrent