#include <stdio.h>

int main()
{
    char a, b;
    a = getc(stdin);
    getc(stdin);
    b = getc(stdin);
    printf("%d", a-b);
    return 0;
}