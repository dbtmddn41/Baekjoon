import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
T = int(f.readline().rstrip())

for _ in range(T):
    n = int(f.readline().rstrip())
    line = [[], []]
    line[0] = list(map(int, f.readline().rstrip().split()))
    line[1] = list(map(int, f.readline().rstrip().split()))

    DP = [[0 for _ in range(3)] for _ in range(n)]
    DP[0][0], DP[0][1], DP[0][2] = line[0][0], line[1][0], 0
    
    for i in range(1, n):
        DP[i][0] = max(DP[i-1][1], DP[i-1][2]) + line[0][i]
        DP[i][1] = max(DP[i-1][0], DP[i-1][2]) + line[1][i]
        DP[i][2] = max(DP[i-1])
        
    print(max(DP[n-1]))