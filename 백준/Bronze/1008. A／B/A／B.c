#include <stdio.h>

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%.10Lf",(long double)a/b);
    return 0;
}