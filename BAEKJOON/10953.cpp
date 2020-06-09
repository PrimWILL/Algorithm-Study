#include <stdio.h>

int main(void){
    int n = 0;
    scanf("%d", &n);

    while(n--){
        int a = 0;
        int b = 0;
        scanf("%d,%d", &a, &b);
        printf("%d\n", a+b);
    }
    return 0;
}