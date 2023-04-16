#include <stdio.h>

void hanoi(int start, int mid, int end, int n)
{
	if (n == 1)
	{
        printf("%d %d\n", start, end);
		return ;
	}
	hanoi(start, end, mid, n-1);
	printf("%d %d\n", start, end);
	hanoi(mid, start, end, n-1);
	return ;
}

int ft_pow(int a, int b)
{
	int total = 1;

	while (b > 0)
	{
		total *= a;
		b--;
	}
	return (total);
}

int main(void)
{
	int s;

	scanf("%d", &s);
	printf("%d\n", ft_pow(2, s) - 1);
	hanoi(1,2,3,s);
}