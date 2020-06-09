#include <stdio.h>

int main(void)
{
    int arr[5];
    scanf("%d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3], &arr[4]);
    int num = 0;
    for(int j = 0; j < 5; j++) 
    {
        num = num + ( arr[j] * arr[j] );
    }
    printf("%d", num % 10);
    return 0;
}