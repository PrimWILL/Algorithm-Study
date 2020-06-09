#include <stdio.h>

int main(void){
    int n = 0;
    scanf("%d", &n);

    if(n % 10 == 2 || n % 10 == 7){
        if((n - 12) >= 0){
            printf("%d", 4 + (n - 12) / 5);
        }
        else{
           printf("-1");
        }
    }
    else if(n % 10 == 1 || n % 10 == 6){
        if((n - 6) >= 0){
            printf("%d", 2 + (n - 6) / 5);
        }
       else{
           printf("-1");
       }
    }
    else if(n % 10 == 3 || n % 10 == 8){
        if((n - 3) >= 0){
            printf("%d", 1 + (n - 3) / 5);
        }
       else{
           printf("-1");
       }
    }
    else if(n % 10 == 4 || n % 10 == 9){
        if((n - 9) >= 0){
            printf("%d", 3 + (n - 9) / 5);
        }
       else{
           printf("-1");
       }
    }
    else{
        printf("%d", n / 5);
    }
    return 0;
}