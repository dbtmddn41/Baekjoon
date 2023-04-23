import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

def can_devide(a, b, W):
    if a + b <= W:
        return 1
    else:
        return 0
    
def solve(DP, base, N, W):
    for i in range(1, N-2):
        DP[i][0] = max(DP[i-1][1], DP[i-1][3]) + can_devide(base[0][i], base[0][i+1], W)
        DP[i][1] = max(DP[i-1][0], DP[i-1][3]) + can_devide(base[1][i], base[1][i+1], W)
        DP[i][2] = DP[i-1][3] + 2 * all((can_devide(base[0][i], base[0][i+1], W), can_devide(base[1][i], base[1][i+1], W)))
        DP[i][3] = max([DP[i-1][3] + can_devide(base[0][i], base[1][i], W)] + DP[i-1])
    

def small_case(base, N, W):
    if N == 1:
        return can_devide(base[0][0], base[1][0], W)
    else:
        res1 = can_devide(base[0][0], base[0][1], W)
        res2 = can_devide(base[1][0], base[1][1], W)
        res3 = can_devide(base[0][0], base[1][0], W)
        res4 = can_devide(base[0][1], base[1][1], W)
        return max((res1 + res2, res3 + res4))

T = int(f.readline().rstrip())

for _ in range(T):
    N, W = map(int, f.readline().rstrip().split())
    base = [[], []]
    base[0] = list(map(int, f.readline().rstrip().split()))
    base[1] = list(map(int, f.readline().rstrip().split()))
    ans = 0
    
    if N <= 2:
        ans = small_case(base, N, W)
        print(2 * N - ans)
        continue

    DP = [[0 for _ in range(4)] for _ in range(N)]
    if can_devide(base[0][0], base[0][N-1], W):
        DP[0][1] = can_devide(base[1][0], base[1][1], W)
        solve(DP, base, N, W)
        DP[N-2][1] = max(DP[N-3][0], DP[N-3][3]) + can_devide(base[1][N-2], base[1][N-1], W)
        DP[N-2][3] = max([DP[N-3][3] + can_devide(base[0][N-2], base[1][N-2], W)] + DP[N-3])
        res = max(DP[N-2][1], DP[N-2][3]) + 1
        ans = max(ans, res)
        
    DP = [[0 for _ in range(4)] for _ in range(N)]
    if can_devide(base[1][0], base[1][N-1], W):
        DP[0][0] = can_devide(base[0][0], base[0][1], W)
        solve(DP, base, N, W)
        DP[N-2][0] = max(DP[N-3][1], DP[N-3][3]) + can_devide(base[0][N-2], base[0][N-1], W)
        DP[N-2][3] = max([DP[N-3][3] + can_devide(base[0][N-2], base[1][N-2], W)] + DP[N-3])
        res = max(DP[N-2][0], DP[N-2][3]) + 1
        ans = max(res, ans)
        
    DP = [[0 for _ in range(4)] for _ in range(N)]
    if can_devide(base[0][0], base[0][N-1], W) and can_devide(base[1][0], base[1][N-1], W):
        solve(DP, base, N, W)
        DP[N-2][3] = max([DP[N-3][3] + can_devide(base[0][N-2], base[1][N-2], W)] + DP[N-3])
        res = DP[N-2][3] + 2
        ans = max(res, ans)
        
    DP = [[0 for _ in range(4)] for _ in range(N)]
    DP[0][0] = can_devide(base[0][0], base[0][1], W)
    DP[0][1] = can_devide(base[1][0], base[1][1], W)
    DP[0][2] = 2 * all((can_devide(base[0][0], base[0][1], W), can_devide(base[1][0], base[1][1], W)))
    DP[0][3] = can_devide(base[0][0], base[1][0], W)
    
    solve(DP, base, N, W)
    DP[N-2][0] = max(DP[N-3][1], DP[N-3][3]) + can_devide(base[0][N-2], base[0][N-1], W)
    DP[N-2][1] = max(DP[N-3][0], DP[N-3][3]) + can_devide(base[1][N-2], base[1][N-1], W)
    DP[N-2][2] = DP[N-3][3] + 2 * all((can_devide(base[0][N-2], base[0][N-1], W), can_devide(base[1][N-2], base[1][N-1], W)))
    DP[N-2][3] = max([DP[N-3][3] + can_devide(base[0][N-2], base[1][N-2], W)] + DP[N-3])
    
    DP[N-1][3] = max([DP[N-2][3] + can_devide(base[0][N-1], base[1][N-1], W)] + DP[N-2])
    res = DP[N-1][3]
    ans = max(res, ans)
    
    print(2 * N - ans)