import numpy as np
f = open('./input2.txt','r').read().strip()
costMap = np.array([[int(c) for c in line] for line in f.split('\n')])
print(costMap)

class node():
    def __init__(self,f,parrent,pos,dirs):
        self.f = f
        self.parrent = parrent
        self.pos = pos
        self.dirs = dirs

openList = [node(0,None,(0,0),[None,None,None])]
closedList = []
found = False
endNode = None
while len(openList) > 0:
    q = min(openList,key=lambda x: x.f)
    openList.remove(q)

    # If goal
    if q.pos == (len(costMap)-1,len(costMap[0])-1):
        endNode = q
        print(q.pos,q.f)
        break

    coords = [((0,1),'R'),((1,0),'D'),((0,-1),'L'),((-1,0),'U')] # R,D,L,U
    for (ry,rx),dir in coords:
        y,x = q.pos
        if y+ry < 0 or y+ry > len(costMap)-1 or x+rx < 0 or x+rx > len(costMap[0])-1:
            continue
        npos = (y+ry,x+rx)
        parrent = q
        penalty = 0
        if (q.dirs[0] == dir and q.dirs[1] == dir and q.dirs[2] == dir) or (q.dirs[2] == 'L' and dir == 'R') or (q.dirs[2] == 'R' and dir == 'L') or (q.dirs[2] == 'D' and dir == 'U') or (q.dirs[2] == 'U' and dir == 'D'):
            penalty = 1000
        f = q.f + costMap[npos[0],npos[1]] + penalty
        ndirs = list(q.dirs)
        ndirs.append(dir)
        ndirs.pop(0)

        skip = False
        # for n in openList:
        #     if n.pos == npos and n.f < f:
        #         skip = True
        for n in closedList:
            if n.pos == npos and n.f < f:
                skip = True
        
        if not skip:
            openList.append(node(f,q,npos,ndirs))
    
    closedList.append(q)
# for n in closedList:
#     print(n.f,n.pos)
# while endNode.parrent is not None:
#     print(endNode.pos,endNode.f,endNode.dirs)
#     endNode = endNode.parrent