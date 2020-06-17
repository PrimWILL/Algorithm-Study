#include <stdio.h>
#include <string.h>

int main(void)
{
    char arr[1000000 + 3];
    scanf("%s", arr);

    arr[strlen(arr)] = '\0';
    arr[strlen(arr) + 1] = '\0';

    switch (strlen(arr) % 3 + 1)
    {
        case 1: 
        for(int i = 0; arr[i] != '\0'; i += 3)
        {
            printf("%d", (arr[i] - '0') * 4 + (arr[i + 1] - '0') * 2 + (arr[i + 2] - '0'));            
        }
        break;
        
        case 2:
        printf("%d", arr[0] - '0');
        for(int i = 1; arr[i] != '\0'; i += 3)
        {
            printf("%d", (arr[i] - '0') * 4 + (arr[i + 1] - '0') * 2 + (arr[i + 2] - '0'));            
        }
        break;

        case 3:
        printf("%d", (arr[0] - '0') * 2 + arr[1] - '0');
        for(int i = 2; arr[i] != '\0'; i += 3)
        {
            printf("%d", (arr[i] - '0') * 4 + (arr[i + 1] - '0') * 2 + (arr[i + 2] - '0'));            
        }
        break;
    }
    return 0;
} 