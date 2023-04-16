import sys
import random
sys.setrecursionlimit(10**4)

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
    
    coprimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
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

def Pollard_rho(n):
    if n % 2 == 0:
        return 2
    if Miller_Rabin_test(n):
        return n
    
    x = random.randrange(2, n+1)
    c = random.randrange(1, 11)
    y = x*x%n + c
    g = 1
    while g == 1:
        g = gcd(abs(y - x), n)
        if g == n:
            x = random.randrange(2, n+1)
            c = random.randrange(1, 11)
            y = x*x%n + c
            g = 1
            continue
        x = x*x%n + c
        y = y*y%n + c
        y = y*y%n + c
    if Miller_Rabin_test(g):
        return g
    else:
        return Pollard_rho(g)

n = int(f.readline().rstrip())

factors = {}
while n > 1:
    p = Pollard_rho(n)
    if p in factors:
        factors[p] += 1
    else:
        factors[p] = 2        
    n //= p

res = 1
for p_n in factors.values():
    res *= p_n
    
print(res)