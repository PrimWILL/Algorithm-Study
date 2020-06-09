#include <stdio.h>
#include <stdlib.h>

int main(void){
    int n;
    scanf("%d", &n);
    int *arr = (int*)malloc(n * sizeof(int));

    for(int i = 0; i < n; i++){
        scanf("%d", &arr[i]);
    }

    int m;
    scanf("%d", &m);
    int *arr2 = (int*)malloc(m * sizeof(int));

    for(int t = 0; t < m; t++){
        scanf("%d", &arr2[t]);
    }

    for(int j = 0; j < m; j++){
        int cp = 0;
        for(int k = 0; k < n; k++){
            if(arr2[j] == arr[k]){
                cp++;
                break;
            }
        }
        if(cp)
            printf("1\n");
        else
        {
            printf("0\n");
        }
    }
    return 0;
}