#include <stdio.h>

int main(void)
{
    char arr[33];
    int code;
    scanf("%s", arr);
    scanf("%d", &code);

    int res = 0;
    for(int i = 0; arr[i] != '\0'; i++)
    {
        if(arr[i] >= '0' && arr[i] <= '9')
        {
            res *= code;
            res += arr[i] - '0';
        }
        else
        {
            res *= code;
            res += (arr[i] - 'A' + 10);
        }
    }
    printf("%d", res);
    return 0;
}