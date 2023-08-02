import sys


f = sys.stdin

N = int(f.readline().rstrip())
A = list(map(int, f.readline().rstrip().split()))
A += [0, 0]
i=0
cost=0
for i in range(N):
    if A[i] and A[i+1] and A[i+2]:
        if A[i+1] > A[i+2]:
            iters = min(A[i], A[i+1] - A[i+2])
            cost += 5 * iters
            A[i] -= iters
            A[i+1] -= iters
        iters = min((A[i], A[i+1], A[i+2]))
        cost += 7 * iters
        A[i] -= iters
        A[i+1] -= iters
        A[i+2] -= iters
    if A[i] and A[i+1]:
        iters = min(A[i], A[i+1])
        cost += 5 * iters
        A[i] -= iters
        A[i+1] -= iters
    if A[i]:
        cost += 3 * A[i]
        A[i] = 0
print(cost)