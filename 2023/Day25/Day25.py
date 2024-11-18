import itertools
class Node():
    def __init__(self,name,set):
        self.name = name
        self.set = set

class Edge():
    def __init__(self,node1,node2):
        self.node1 = node1
        self.node2 = node2

f = open('./input2.txt','r').read().strip()
node_set = list(set(sum([line.replace(':','').split(' ') for line in f.split('\n')],[])))
nodes = []
for n in node_set:
    nodes.append(Node(n,'A'))
# for n in nodes:
#     print(n.name)

edges = []
for line in f.split('\n'):
    node1, other_nodes = line.split(': ')
    for node2 in other_nodes.split(' '):
        if not any([(e.node1.name == node1 and e.node2.name == node2) or (e.node1.name == node2 and e.node2.name == node1) for e in edges]):
            for n in nodes:
                if n.name == node1:
                    n1 = n
            for n in nodes:
                if n.name == node2:
                    n2 = n
            edges.append(Edge(node1=n1,node2=n2))
# for e in edges:
#     print(e.node1.name, e.node2.name)

# nodes = [Node('A','A'),Node('B','A'),Node('C','A')]

# for i in range(len(nodes)):
for L in range(len(nodes) + 1):
    for subset in itertools.combinations(nodes, L):
    # for node in nodes[i:]:
        for n in subset:
            n.set = 'B'
        found = []
        for e in edges:
            if e.node1.set != e.node2.set:
                found.append(e)
        if len(found) == 3:
            print('Found:')
            for f in found:
                print(f.node1.name,f.node2.name)
            print('A:')
            A = 0
            for n in nodes:
                if n.set == 'A':
                    A += 1
                    print(n.name)
            print('B:')
            B = 0
            for n in nodes:
                if n.set == 'B':
                    B += 1
                    print(n.name)
            print(A*B)
            break
        for n in nodes:
            n.set = 'A'




# stuff = [1, 2, 3, 4]
# for L in range(len(stuff) + 1):
#     for subset in itertools.combinations(stuff, L):
#         print(subset)
# a
# a b
# a b c
# b
# b c
# c
                
# a
# a b
# a c
# a d
# a b c
# a b d
# a b c d
# b
# b c
# b d
# b c d
# c
# c d
# d
                # a a a a
                # b a a a
                # a b a a
                # a a b a
                # a a a b
                # a b a a
                # a b b a
                # a b a b
                # a a b b 
                # b b a a
                # b a b a
                # b a a b
                # b b b a
                # b b a b
                # b b b a
                # b b b b

                 