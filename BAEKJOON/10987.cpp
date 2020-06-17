#include <stdio.h>

int main(void){
    int c;
    int vowel = 0;
    c = getchar();
    while(c != '\n'){
        if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            vowel++;
        c = getchar();
    }
    printf("%d", vowel);
    return 0;
}