import sys

is_boj = 1
if is_boj:
    f = sys.stdin
else:
    f = open("input.txt", "rt")

def power(a, b, n):
    a %= n
    res = 1 
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % n
        a = (a * a) % n
        b //= 2
    return res

def gcd(n, m):
    if n < m:
        n, m = m, n
    
    while m != 0:
        tmp = m
        m = n % m
        n = tmp
    return n
        
def Miller_Rabin_test(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    coprimes = [2, 7, 61]
    for a in coprimes:
        if a == n:
            continue
        k = n - 1
        while True:
            res = power(a, k, n)
            if res == n-1:
                break
            if k % 2 == 1:
                if res == 1 or res == n-1:
                    break
                else:
                    return False
            k //= 2
                
    return True

N = int(f.readline().rstrip())

kwang = 0
for _ in range(N):
    A = int(f.readline().rstrip())
    if Miller_Rabin_test(2*A + 1):
        kwang += 1
print(kwang)