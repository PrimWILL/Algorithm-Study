#include <stdio.h>

int main(void){
    char a;
    while(scanf("%c", &a) != EOF){
        printf("%c", a);
    }
    return 0;
}

/* int main(void){
    int a;
    while((c = getchar()) != EOF)
        putchar(c);
    return 0;
}
*/