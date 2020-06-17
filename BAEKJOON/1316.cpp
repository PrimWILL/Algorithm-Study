#include <stdio.h>

int main(void){
    int n = 0;
    scanf("%d", &n);
    int cnt = 0;

    while(n--){
        char arr[100];
        scanf("%s", arr);

        int alpha[26] = {0};
        char temp = arr[0];
        int t = 0;

        for(int i = 0; arr[i] != NULL; i++){
            if(alpha[arr[i] - 'a'] >0){
                if(arr[i] == temp){
                    alpha[arr[i] - 'a']++;
                }
                else{
                    t++;
                    break;
                }
            }
            else{
                alpha[arr[i]-'a']++;
            }
            temp = arr[i];
        }

        if(t == 0){
            cnt++;
        }
    }
    printf("%d", cnt);
    return 0;
}