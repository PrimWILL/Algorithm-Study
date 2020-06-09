#include <stdio.h>

int main(void)
{
    char board[8][9];
    for(int i = 0; i < 8; i++)
    {
        scanf("%s", board[i]);
    }

    int cnt = 0;
    for(int j = 0; j < 8; j++)
    {
        if(j % 2 == 0)
        {
            for(int k = 0; k < 8; k += 2)
            {
                if(board[j][k] == 'F') { cnt++; }
            }
        }
        else
        {
            for(int k = 1; k < 8; k += 2)
            {
                if(board[j][k] == 'F') { cnt++; }
            }
        }
    }
    printf("%d", cnt);
    return 0;
}