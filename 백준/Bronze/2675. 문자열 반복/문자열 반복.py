T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    ans = ''
    for c in S:
        ans += c*R
    print(ans)
    