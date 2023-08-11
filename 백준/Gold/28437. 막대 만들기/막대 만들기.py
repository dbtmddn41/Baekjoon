import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

N = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))

Q = int(f.readline().rstrip())
L = list(map(int, f.readline().rstrip().split()))

K = max(A + L)

DP = [0 for _ in range(K+1)]
for a in A:
    DP[a] = 1
for i in range(1, K+1):
    for j in range(2*i, K+1, i):
        DP[j] += DP[i]
print(*(DP[l] for l in L))
