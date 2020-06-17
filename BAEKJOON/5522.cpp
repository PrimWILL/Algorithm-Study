#include <stdio.h>

int main(void)
{
    int n;
    int res = 0;
    for(int i = 0; i < 5; i++)
    {
        scanf("%d", &n);
        res += n;
    }
    printf("%d", res);
    return 0;
}