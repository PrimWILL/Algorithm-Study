#include <stdio.h>

int main(void){
    int n;
    scanf("%d", &n);
    int cute = 0;
    int not_cute = 0;
    int temp;
    while(n--){
        scanf("%d", &temp);
        if(temp == 1)
            cute++;
        else
            not_cute++;
    }
    if(cute > not_cute)
        printf("Junhee is cute!");
    else
    {
        printf("Junhee is not cute!");
    }
    return 0;
}