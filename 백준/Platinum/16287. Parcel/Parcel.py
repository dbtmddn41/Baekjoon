import sys
import bisect
is_boj = 1
if is_boj:
	f = sys.stdin
else:
	f = open("input.txt", "rt")

def main():
    w, n = map(int, f.readline().rstrip().split())
    A = list(map(int, f.readline().rstrip().split()))

    A.sort()
    end = bisect.bisect_left(A, w)
    sums = [0 for _ in range(w)]

    for i in range(1, end):
        for j in range(i):
            s = A[i] + A[j]
            if s < w:
                sums[s] = 1
            else:
                break
        #i를 기준으로 나눈 것이므로 i+1은 포함된다 생각해도 된다.
        for j in range(i+2, end):
            s = A[i+1] + A[j]
            if s < w:
                if sums[w - s] == 1:
                    print('YES')
                    return
            else:
                break
    print("NO")
                
main()