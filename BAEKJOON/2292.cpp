#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);

    if(n == 1) 
    { 
        printf("1"); 
    }

    else
    {
        for(int i = 2; ; i++)
        {
            if(n >= (2 + 3 * (i - 2) * (i - 1)) && n < (2 + 3 * (i - 1) * i))
            { 
                printf("%d", i);
                break;
            }
        }
    }
    return 0;
}