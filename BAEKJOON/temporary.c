#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int hey[1] = {100};
    int *p = &hey[0];
    printf("%d %d\n", *p, p[0]);
    free(p);
    return 0;
}