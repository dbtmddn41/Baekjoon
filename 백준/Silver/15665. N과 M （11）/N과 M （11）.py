import sys

is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

N, M = map(int, f.readline().rstrip().split())
nums = list(map(str, sorted(list(set(map(int, f.readline().rstrip().split()))))))
N = len(nums)
def dfs(s, depth):
    if depth == M:
        print(s[:-1])
        return
    
    for i in range(0, N):
        new_s = s + nums[i] + ' '
        dfs(new_s, depth+1)
        
s = ''
dfs(s, 0)