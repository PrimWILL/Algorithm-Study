#include <stdio.h>

int main(void)
{
    char str[100];
    scanf("%s", str);
    int arr[26] = { 0 };

    for(int i = 0; str[i] != '\0'; i++)
    {
        arr[str[i] - 'a']++;
    }
    for(int j = 0; j < 26; j++)
    {
        printf("%d ", arr[j]);
    }
    return 0;
}