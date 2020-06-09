#include <stdio.h>

int main(void){
    char i;
    i = getchar();

    while(i != EOF)
    {
        putchar(i);
        i = getchar();
    }
    return 0;
}