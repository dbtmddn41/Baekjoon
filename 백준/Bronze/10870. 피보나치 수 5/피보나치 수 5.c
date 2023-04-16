#include <stdio.h>

int fibo(int n)
{
    if (n == 1 || n ==0)
        return (n);
    return (fibo(n-1) + fibo(n-2));

}

int main(void)
{
    int    n;
    
    scanf("%d", &n);
    printf("%d", fibo(n));
    return (0);
}