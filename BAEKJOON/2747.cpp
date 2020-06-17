#include <stdio.h>

int fibo(int n){
    if(n < 2) return n;
    
    int num1 = 0;
    int num2 = 1;
    int res = 0;

    for(int i = 2; i <= n; i++){
        res = num1 + num2;
        num1 = num2;
        num2 = res;
    }
    return res;
}

int main(void){
    int n;
    scanf("%d", &n);
    printf("%d", fibo(n));
    return 0;
}