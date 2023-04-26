import sys
from collections import deque

sys.setrecursionlimit(10**6)
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

 
N, M = map(int, f.readline().rstrip().split())

board = []
for _ in range(N):
    line = list(f.readline().rstrip())
    board.append(line)
    
DP = [[0 for _ in range(M)] for _ in range(N)]
dp_id = 0
visited = [[0 for _ in range(M)] for _ in range(N)]
stack = []
def dfs(i, j, depth):
    if DP[i][j] != 0:
        return DP[i][j]
    if visited[i][j] != 0:
        return 0, -1
    visited[i][j] = 1
    if depth > 0:
        stack.append((i,j))
    res = 1
    ids = set()
    for di, dj in ((1, 0), (0, -1), (-1, 0), (0, 1)):
        if 0<=i+di<N and 0<=j+dj<M:
            if board[i+di][j+dj] == '0':
                a, dpid = dfs(i+di, j+dj, depth+1)
                if dpid == -1 or dpid not in ids:
                    res += a
                    ids.add(dpid)
                    
    if depth == 1:
        global dp_id
        while stack:
            i ,j = stack.pop()
            DP[i][j] = (res, dp_id)
        dp_id += 1
        return res, dp_id-1
    return res, -1

ans = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == '1':
            res, _ = dfs(i, j, 0)
            ans[i][j] = str(res%10)
        else:
            ans[i][j] = '0'
print(*map(lambda x: ''.join(x), ans), sep='\n')