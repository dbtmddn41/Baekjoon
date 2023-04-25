import sys
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
N = int(f.readline().rstrip())
board = []
for _ in range(N):
    line = list(map(int, f.readline().strip().split()))
    board.append(line)

ru = [1 for _ in range(2 * N + 1)]
lu = [1 for _ in range(2 * N + 1)]

def search(i, j):
    if i >= N:
        return 0
    if j < N-2:
        next_i, next_j = i, j+2
    else:
        next_i, next_j = i+1, int(not j%2)
    res = 0
    if board[i][j] == 1 and ru[i+j] and lu[i-j+N]:
        ru[i+j] = 0
        lu[i-j+N] = 0
        res = search(next_i, next_j) + 1
        ru[i+j] = 1
        lu[i-j+N] = 1
    
    res = max(res, search(next_i, next_j))
    return res

print(search(0, 0) + search(0,1))
        