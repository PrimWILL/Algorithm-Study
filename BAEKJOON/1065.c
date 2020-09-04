#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

void AP(int num)
{   
    int cnt = 0;
    if (num < 100) cnt = num;
    else {
        cnt = 99;
        for (int i = 100; i <= num; i++) {
            int n1, n2, r, temp = i;
            bool cp = true;
            n1 = temp % 10;
            temp /= 10;
            n2 = temp % 10;
            r = n1 - n2;
            while (temp/10 != 0) {
                n1 = n2;
                temp /= 10;
                n2 = temp % 10;
                if (r != (n1 - n2)) {
                    cp = false;
                    break;
                }
            }
            if (cp) {
                cnt++;
            }
        }
    }
    printf("%d\n", cnt);
}

int main(void)
{
    int n;
    scanf("%d", &n);
    AP(n);

    return 0;
}