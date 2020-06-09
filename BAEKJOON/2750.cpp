#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n;
    scanf("%d", &n);

    int *arr = (int*)malloc(sizeof(int) * n);

    for(int i = 0; i < n; i++) { scanf("%d", &arr[i]); }

    for(int j = 0; j < n; j++){
        for(int k = 0; k < n - j - 1; k++)
        {
            if (arr[k] > arr[k + 1]){
                int temp = arr[k];
                arr[k] = arr[k + 1];
                arr[k + 1] = temp;
            }
        }
    }

    for(int t = 0; t < n; t++) { printf("%d\n", arr[t]); }
    return 0;
}