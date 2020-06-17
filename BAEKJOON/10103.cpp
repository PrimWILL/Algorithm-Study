#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int score1 = 100;
    int score2 = 100;
    
    while(n--){
        int a, b;
        scanf("%d %d", &a, &b);
        if(a > b)
            score2 -= a;
        else if(a < b)
            score1 -= b;
    }
    printf("%d\n%d\n", score1, score2);
    return 0;
}