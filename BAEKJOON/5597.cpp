#include <stdio.h>

int main(void){
    char arr[30] = { 0 };
    int n;
    for(int i = 0; i < 28; i++){
        scanf("%d", &n);
        arr[n - 1]++;
    }
    for(int j = 0; j < 30; j++){
        if(arr[j] == 0)
            printf("%d\n", j + 1);
    }
    return 0;
}