#include <stdio.h>
#include <string.h>
#pragma warning(disable: 4996)
#define MAX 1000000

void hanoi_tower(int n, char from, char tmp, char to)
{
    if(n == 1)
    {
        printf("%c %c\n", from, to);           // from에 위치한 맨 아래 원판을 to로 옮긴다
    }
    else
    {
        hanoi_tower(n - 1, from, to, tmp);     // 1. from에 위치한, 맨 아래 원판을 제외한 모든 원판을 tmp로 옮김
        printf("%c %c\n", from, to);           // 2. from에 위치한 맨 아래 원판을 to로 옮긴다
        hanoi_tower(n - 1, tmp, from, to);     // 3. tmp에 위치한 원판을 to로 옮긴다
    }
}

double power(int x, int n)
{
    if (n == 0) return 1;
    else if (n % 2 == 0) return power(x * x, n / 2);
    else return (x * power(x * x, (n - 1) / 2));
}

int main(void)
{
    int n = 0;
    char result[MAX];
    double tmp = 0;
    scanf("%d", &n);

    tmp = power(2, n);

    sprintf(result, "%.0f", tmp);
    int size = strlen(result);
    result[size - 1] = (char)(((int)result[size - 1] - '0' - 1) + '0');
    printf("%s\n", result);
    
    if(n <= 20)
        hanoi_tower(n, '1', '2', '3');
    return 0;
}