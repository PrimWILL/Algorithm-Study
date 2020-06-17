#include <stdio.h>

int main(void)
{
    int num = 0;
    int a;
    for(int i = 0; i < 4; i++) 
    { 
        scanf("%d", &a);
        num += a;
    }

    printf("%d\n", num / 60);
    printf("%d", num % 60);
    return 0;
}