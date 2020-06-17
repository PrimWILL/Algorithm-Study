#include <stdio.h>

int main(void)
{
    char arr[100];
    scanf("%s", arr);

    int cnt = 0;
    for(int i = 0; arr[i] != '\0'; i++)
    {
        printf("%c", arr[i]);
        cnt++;
        if(cnt % 10 == 0) { printf("\n"); }
    }
    return 0;
}