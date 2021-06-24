#include <iostream>
using namespace std;

int main()
{
    int chk[100], num, ans;
    
    for (int i = 0; i < 4; i++) 
    {
        scanf("%d", &num);
        chk[num]++;
    }

    for (int i = 0; i < 5; i++)
    {
        scanf("%d", &num);
        if (!chk[num]) ans++;
    }

    cout << ans << endl;
    return 0;
}