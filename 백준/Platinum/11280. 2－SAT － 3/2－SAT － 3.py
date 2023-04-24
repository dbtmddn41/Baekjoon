import sys
sys.setrecursionlimit(10**6)
is_boj = 1

if is_boj:
    f = sys.stdin
else:
    f = open("./input.txt", "rt")
    
N, M = map(int, f.readline().rstrip().split())
graph = [[] for _ in range(2*N)]

for _ in range(M):
    a, b = map(int, f.readline().rstrip().split())
    graph[abs(a)-1 + N*(a>0)].append((abs(b)-1) + N*(b<0))
    graph[abs(b)-1 + N*(b>0)].append((abs(a)-1) + N*(a<0))
    
sat = 1

stack = []
node_id = 0
ids = [-1 for _ in range(2*N)]
on_stack = [-1 for _ in range(2*N)]

def search(node):
    global stack, node_id, ids, on_stack, sat
    ids[node] = node_id
    res = node_id
    node_id += 1
    stack.append(node)
    on_stack[node] = 1
    
    for succ in graph[node]:
        if ids[succ] == -1:
            res = min(search(succ), res)
        elif on_stack[succ] != -1:
            res = min(res, ids[succ])
            
    if res == ids[node]:
        scc= set()
        w = stack.pop()
        while w != node:
            scc.add(w)
            on_stack[w] = -1
            w = stack.pop()
            if w + N in scc or w - N in scc:
                sat = 0
        on_stack[w] = -1
        
    return res

for v in range(2*N):
    if ids[v] == -1:
        search(v)
        
    if sat == 0:
        break

print(sat)