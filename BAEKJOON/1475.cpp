#include <stdio.h>

int main(void)
{
    char arr[1000000];
    scanf("%s", arr);

    int num[10];
    for(int i = 0; arr[i] != '\0'; i++)
    {
        num[arr[i] - '0']++;
    }

    num[6] = (num[6] + num[9]) / 2 + (num[6] + num[9]) % 2;
    num[9] = 0;
    
    int res = 0;
    for(int j = 0; j < 10; j++)
    {
        if(res < num[j]){
            res = num[j];
        }
    }
    printf("%d", res);
    return 0;
}