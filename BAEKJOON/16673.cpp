#include <stdio.h>

int main(void){
    int c, k, p;
    scanf("%d %d %d", &c, &k, &p);
    int res = 0;
    for(int i = 1; i <= c; i++){
        res = res + k * i + p * i * i;
    }
    printf("%d", res);
    return 0;
}