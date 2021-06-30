#include <stdio.h>

int main()
{
    int A, B, V;
    scanf("%d %d %d", &A, &B, &V);
    V -= A;
    int result = V / (A - B);

    if (V == 0) 
        printf("1");
    else if (V % (A - B) > 0)
        printf("%d", result + 2);
    else
        printf("%d", result + 1);
    return 0;
}