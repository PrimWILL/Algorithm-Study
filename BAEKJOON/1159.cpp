#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    int c;
    while((c = getchar()) != '\n');

    int arr[26] = { 0 };
    while(n--)
    {
        c = getchar();
        arr[c - 'a']++;
        while((c = getchar()) != '\n');
    }
    int cnt = 0;
    for(int i = 0; i < 26; i++)
    {
        if(arr[i] >= 5) 
        { 
            printf("%c", i + 'a');
            cnt++;
        }
    }
    if(cnt == 0) { printf("PREDAJA"); }
    return 0;
}