#include <stdio.h>
#define MIN(a, b) ((a) < (b) ? (a) : (b))

int main(void) {
    int set[5];
    for(int i = 0; i < 5; i++)
        scanf("%d", &set[i]);
    int min = MIN(set[0], set[1]);
    min = MIN(min, set[2]);
    min = min + MIN(set[3], set[4]) - 50;
    printf("%d\n", min);
    return 0;
}