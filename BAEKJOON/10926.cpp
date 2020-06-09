#include <stdio.h>

int main(void){
    int c;
    while((c = getchar()) != '\n'){
        putchar(c);
    }
    printf("?\?!");
    return 0;
}