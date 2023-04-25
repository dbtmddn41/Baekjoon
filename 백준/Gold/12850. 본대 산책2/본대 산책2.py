import sys
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

D = int(f.readline().rstrip())

def matmul(A, B):
    result = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            s = 0
            for k in range(8):
                s += (A[i][k] * B[k][j]) % 1_000_000_007
            result[i][j] = s
    return result

sungsil_univ = [[0, 1, 0, 1, 0, 0, 0, 0],   #학생회관
                [1, 0, 1, 0, 1, 0, 0, 0],   #진리관
                [0, 1, 0, 0, 1, 1, 1, 0],   #신양관
                [1, 0, 0, 0, 1, 0, 0, 0],   #형남공학관
                [0, 1, 1, 1, 0, 0, 1, 0],   #한경직기념관
                [0, 0, 1, 0, 0, 0, 1, 1],   #전산관
                [0, 0, 1, 0, 1, 1, 0, 1],   #미래관
                [0, 0, 0, 0, 0, 1, 1, 0]    #정보과학관
                ]
Identity = [[0 if i != j else 1 for j in range(8) ] for i in range(8)]

def power(A, d):
    res = Identity[:]
    while d > 0:
        if d & 1:
            res = matmul(res, A)
        A = matmul(A, A)
        d >>= 1
    return res

res = power(sungsil_univ, D)
print(res[7][7] % 1_000_000_007)