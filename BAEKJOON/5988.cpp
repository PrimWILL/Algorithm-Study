#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);

    while(n--){
        int c = 0;
        int t = 0;
        t = getchar();
        while(1){
            c = getchar();
            if(c == '\n')
                break;
            t = c;
        }
        if(t % 2 == 0)
            printf("even\n");
        else
        {
            printf("odd\n");
        }
    }
    return 0;
}