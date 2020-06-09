#include <stdio.h>

int main(void)
{
    int arr[6] = {1, 1, 2, 2, 2, 8};
    int cf[6];
    for(int i = 0; i < 6; i++) { scanf("%d", &cf[i]); }
    for(int j = 0; j < 6; j++) { printf("%d ", arr[j] - cf[j]); }
    return 0;
}