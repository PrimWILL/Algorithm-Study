#include <stdio.h>

int main(void){
    int arr[9][9];
    for(int i = 0; i < 9; i++){
        for(int j = 0; j < 9; j++){
            scanf("%d", &arr[i][j]);
        }
    }
    int max = 0;
    int row = 0;
    int column = 0;

    for(int m = 0; m < 9; m++){
        for(int n = 0; n < 9; n++){
            if(arr[m][n] > max){
                max = arr[m][n];
                row = m;
                column = n;
            }
        }
    }
    printf("%d\n", max);
    printf("%d %d\n", row + 1, column + 1);
    return 0;
}