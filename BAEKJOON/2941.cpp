#include <stdio.h>

int main(void){
    char arr[100];
    scanf("%s", arr);

    int cnt = 0;
    for(int i = 0; arr[i] != NULL; i++)
    {
        if(arr[i] == '=')
        {
            if(arr[i-1] == 'z')
            {
                if(arr[i-2] == 'd')
                {
                    cnt -= 2;
                }

                else
                {
                    cnt--;
                }
                
            }

            else
            {
                cnt--;
            }
            
        }
        else if (arr[i] == '-'){
            cnt--;
        }
        else if(arr[i] == 'j'){
            if(arr[i-1] == 'l' || arr[i-1] == 'n'){
                cnt--;
            }
        }
        cnt++;
    }
    printf("%d", cnt);
    return 0;
}