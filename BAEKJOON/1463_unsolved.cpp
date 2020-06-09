#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    int cnt = 0;
    while (n != 1) {
        if(n % 3 == 0){
            n /= 3;
            printf("first: %d ", n);
            cnt++;
        }
        else if(n % 2 == 0){
            n /= 2;
            printf("second: %d ", n);
            cnt++;
        }
        else
        {
            n -= 1;
            printf("Third: %d ", n);
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}
