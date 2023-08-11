import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
def main():
    global f
    N, M = map(int, f.readline().rstrip().split())
    matrix = []
    curr_line = row_delta = col_delta = None
    cnt = {0: 1}
    try:
        for i in range(N):
            curr_line = list(map(int, f.readline().rstrip().split()))
            matrix.append(curr_line)
            if i == 0:
                for c in curr_line:
                    cnt[c] = cnt.get(c, 0) + 1
                col_delta = [curr_line[i+1]-curr_line[i] for i in range(M-1)]
            else:
                row_delta = matrix[0][0] - curr_line[0]
                cnt[row_delta] = cnt.get(row_delta, 0) + 1
                for j in range(1, M):
                    if matrix[0][j] - curr_line[j] != row_delta or curr_line[j] - curr_line[j-1] != col_delta[j-1]:
                            raise
    except:
        print(-1)
        return
    max_val, max_cnt = max(cnt.items(), key=lambda x: x[1])
    print(N + M - max_cnt)
    
    for i in range(N):
        delta = max_val - (matrix[0][0] - matrix[i][0])
        if delta != 0:
            print(1, i+1, delta)
    for j in range(M):
        delta = max_val - matrix[0][j]
        if delta != 0:
            print(2, j+1, -delta)
    
    
if __name__ == '__main__':
    main()