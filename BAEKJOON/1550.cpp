#include <stdio.h>

int main(void)
{
    int c;
    int res = 0;
    while((c = getchar()) != '\n')
    {
        res *= 16;
        if(c >= '0' && c <= '9') { res = res + c - '0'; }
        else { res = res + (c - 'A' + 10); }
    }
    printf("%d", res);
    return 0;
}