import sys
import heapq

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")
    
n = int(f.readline().rstrip())
loc = []
for _ in range(n):
    h, o = map(int, f.readline().rstrip().split())
    if h > o:
        h, o = o, h
    loc.append((h, o))

d = int(f.readline().rstrip())
loc.sort(key = lambda x:x[1])

start = loc[0][1] - d
heap = []

ans = 0
heapq.heappush(heap, loc[0])
i = 0
while i < n:
    while heap and heap[0][0] < start:
        heapq.heappop(heap)
    ans = max(ans, len(heap))

    i += 1
    if i < n:
        heapq.heappush(heap, loc[i])
        start = loc[i][1] - d
    while i + 1 < n and start == loc[i+1][1] - d:
        i += 1
        heapq.heappush(heap, loc[i])
        
print(ans)