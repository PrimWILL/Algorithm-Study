#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    while(n--){
        int t;
        scanf("%d", &t);
        while(t--)
            printf("=");
        printf("\n");
    }
    return 0;
}