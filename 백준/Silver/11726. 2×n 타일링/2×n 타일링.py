import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
n = int(f.readline().rstrip())

DP = [0 for _ in range(n)]

DP[0] = 1
if n > 1:
    DP[1] = 2
for i in range(2, n):
    DP[i] = (DP[i-1] + DP[i-2]) % 10007

print(DP[n-1])