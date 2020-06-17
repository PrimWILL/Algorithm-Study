#include <stdio.h>

int BC(int N, int K){
    if(K == 0 || K == N) return 1;
    else return BC(N-1, K-1) + BC(N-1, K);
}

int main(void)
{
    int N, K;
    scanf("%d %d", &N, &K);
    printf("%d", BC(N, K));
    return 0;
}