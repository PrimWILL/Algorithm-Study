#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);
    while(t--)
    {
        int k, n;
        scanf("%d", &k);
        scanf("%d", &n);

        int arr[k][n] = { 0 };

        for(int i = 0; i < n; i++)
        {
            arr[0][i] = i + 1;
        }

        for(int i = 1; i < k; i++)
        {
            for(int j = 0; j < n; j++)
            {
                int res = 0;
                for(int k = 0; k < j; k++)
                {
                    res += arr[i - 1][k];
                }
                arr[i][j] = res;
            }
        }

        printf("%d", arr[k][n]);
    }
    return 0;
}