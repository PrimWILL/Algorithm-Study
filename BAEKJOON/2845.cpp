#include <stdio.h>

int main(void)
{
    int a, b;
    scanf("%d %d", &a, &b);

    int res = a * b;

    int arr[5];
    for(int i = 0; i < 5; i++) { scanf("%d", &arr[i]); }

    int arr_res[5];
    for(int j = 0; j < 5; j++) { arr_res[j] = arr[j] - res; }
    for(int k = 0; k < 5; k++) { printf("%d ", arr_res[k]); }
    return 0;
}