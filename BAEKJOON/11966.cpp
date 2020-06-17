#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    if(n == (n & -n))
        printf("1\n");
    else 
        printf("0\n");
    return 0;
}