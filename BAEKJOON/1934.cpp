#include <stdio.h>

int GCD(int a, int b)
{
    if(a % b == 0) return b;
    else return GCD(b, a % b);
}

int main(void)
{
    int T;
    scanf("%d", &T);

    while(T--)
    {
        int a, b;
        scanf("%d %d", &a, &b);

        int gcd_num = 0;
        if(a > b) { gcd_num = GCD(a, b); }
        else { gcd_num = GCD(b, a); }
        int lcd_num = a * b / gcd_num;;
        printf("%d\n", lcd_num);
    }
    return 0;
}