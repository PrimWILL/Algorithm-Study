#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        for(int k = 0; k < i; k++){
            printf(" ");
        }
        for(int j = 0; j < 2 * (n - i) - 1; j++){
            printf("*");
        }
        printf("\n");
    }
    for(int l = 0; l < n - 1; l++){
        for(int m = 0; m < n - l - 2; m++){
            printf(" ");
        }
        for(int t = 0; t < 2 * (l + 2) - 1; t++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}