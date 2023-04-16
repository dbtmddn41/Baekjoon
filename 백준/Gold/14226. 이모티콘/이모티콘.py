import sys
from collections import deque
import bisect

is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")
 
S = int(f.readline().rstrip())

def bi_in(l, element):
    return bisect.bisect_right(l, element) - bisect.bisect_left(l, element)

q = deque()

n=1
q.append((n, 0))
visited = {}
visited[(1, 0)] = 0
while n != S:
    n, cb = q.popleft()

    t = visited[(n, cb)]
    
    if (n, n) not in visited:
        q.append((n, n))
        visited[(n, n)] = t + 1
    
    if (n+cb, cb) not in visited:
        q.append((n+cb, cb))
        visited[(n+cb, cb)] = t + 1

    if (n-1, cb) not in visited:
        q.append((n-1, cb))
        visited[(n-1, cb)] = t + 1
print(t)