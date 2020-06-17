#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n - i -1; j++)
        {
            printf(" ");
        }
        for(int k = 0; k < (i + 1) * 2 - 1; k++){
            printf("*");
        }
        printf("\n");
    }
    for(int t = n - 1; t > 0; t--){
        for(int m = 0; m < n - t; m++)
        {
            printf(" ");
        }
        for(int p = 0; p < t * 2 - 1; p++)
        {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}