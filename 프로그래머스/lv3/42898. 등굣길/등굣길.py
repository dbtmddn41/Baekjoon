mod = 1_000_000_007

def solution(m, n, puddles):
    global mod
    answer = 0
    DP = [[-1 for _ in range(m)] for _ in range(n)]
    for i, j in puddles:
        DP[j-1][i-1] = 0
    
    tmp = 1
    for i in range(n):
        if DP[i][0] != -1:
            tmp = 0
            continue
        DP[i][0] = tmp
    tmp = 1
    for j in range(1, m):
        if DP[0][j] != -1:
            tmp = 0
            continue
        DP[0][j] = tmp
    
    for i in range(1, n):
        for j in range(1, m):
            if DP[i][j] == -1:
                DP[i][j] = (DP[i][j-1] + DP[i-1][j]) % mod
    answer = DP[n-1][m-1] % mod
    return answer