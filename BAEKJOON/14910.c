#include <stdio.h>
#include <string.h>

int main(void)
{
    int current, next;
    scanf("%d", &current);
    while (scanf("%d", &next) != EOF) {
        if (current > next) {
            printf("Bad\n");
            return 0;
        }
        else current = next;
    }

    /*int num[1000000];
    int end, cp = -1;
    for (end = 0; scanf("%d", &num[end]) != EOF; end++)
    
    if (end) {
        for (int i = 0; i < end; i++) {
            if (!compare(num[i], num[i + 1])) {
                printf("Bad\n");
                return 0;
            }
        }
    }*/
    printf("Good\n");
    return 0;
}