#include <stdio.h>
#include <wchar.h>

int main(void)
{
    wchar_t a[4];
    wscanf(L"%s", &a);
    wprintf(L"%d\n", a - 44031);
    return 0;
}