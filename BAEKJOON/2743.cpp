#include <stdio.h>

int main(void){
    int cnt = 0;
    char arr[100];
    scanf("%s", arr);
    for(int i = 0; arr[i] != '\0'; i++)
        cnt++;
    printf("%d\n", cnt);
    return 0;
}