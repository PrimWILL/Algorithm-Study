#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    for(int i = 0; i < n; i++){
        for(int k = 0; k < i + 1; k++){
            printf("*");
        }
        printf("\n");
    }
    for(int j = n - 1; j > 0; j--){
        for(int t = 0; t < j; t++){
            printf("*");
        }
        printf("\n");
    }
    return 0;
}