#include <stdio.h>

int gcd_algo(int a, int b){
    return b ? gcd_algo(b, a % b) : a;
}

int lcm_algo(int a, int b, int gcd){
    return a * b / gcd;
}

int main(void){
    int a, b;
    scanf("%d %d", &a, &b);

    int gcd = 0;
    int lcm = 0;

    if(b > a)
        gcd = gcd_algo(b, a);
    else
        gcd = gcd_algo(a, b);
    lcm = lcm_algo(a, b, gcd);

    printf("%d\n%d\n", gcd, lcm);
    return 0;
}