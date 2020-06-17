#include <stdio.h>
#include <string.h>

int main(void){
    char arr[100];
    scanf("%s", arr);
    int n = strlen(arr);
    int cp = 1;
    for(int i = 0; i < n / 2; i++){
        if(arr[i] != arr[n - i - 1]){
            cp = 0;
            break;
        }
    }
    printf("%d", cp);
    return 0;
}