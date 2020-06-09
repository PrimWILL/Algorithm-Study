#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int N;
    int *age = (int*)malloc(sizeof(int) * N);
    char **name = (char**)malloc(sizeof(char*) * N);
    for(int i = 0; i < N; i++)
    {
        name[i] = (char*)malloc(sizeof(char) * 101);
    }
}