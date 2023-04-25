import sys
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
n, m = map(int, f.readline().rstrip().split())
sungsil_univ = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, f.readline().rstrip().split())
    sungsil_univ[a-1][b-1] = 1
    sungsil_univ[b-1][a-1] = 1

D = int(f.readline().rstrip())

def matmul(A, B):
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            s = 0
            for k in range(n):
                s += (A[i][k] * B[k][j]) % 1_000_000_007
            result[i][j] = s
    return result

Identity = [[0 if i != j else 1 for j in range(n) ] for i in range(n)]

def power(A, d):
    res = Identity[:]
    while d > 0:
        if d & 1:
            res = matmul(res, A)
        A = matmul(A, A)
        d >>= 1
    return res

res = power(sungsil_univ, D)
print(res[0][0] % 1_000_000_007)
