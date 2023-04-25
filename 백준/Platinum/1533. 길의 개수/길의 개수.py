import sys
import bisect
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N, S, E, T = map(int, f.readline().rstrip().split())
graph = [[0 for _ in range(5*N)] for _ in range(5*N)]

for start in range(N):
    line = list(map(int, tuple(f.readline().rstrip())))
    for i in range(N):
        if line[i] == 0:
            continue
        graph[5*start+4][5*i+5-line[i]] = 1
        for j in range(5-line[i], 4):
            graph[5*i+j][5*i+j+1] = 1
            
def matmul(A, B):
    result = [[0 for _ in range(5*N)] for _ in range(5*N)]
    for i in range(5*N):
        for j in range(5*N):
            s = 0
            for k in range(5*N):
                s += (A[i][k] * B[k][j]) % 1_000_003
            result[i][j] = s
    return result

Identity = [[0 if i != j else 1 for j in range(5*N) ] for i in range(5*N)]

def power(A, d):
    res = Identity[:]
    while d > 0:
        if d & 1:
            res = matmul(res, A)
        A = matmul(A, A)
        d >>= 1
    return res

res = power(graph, T)
print(res[5*S-1][5*E-1] % 1_000_003)
