#include <iostream>
using namespace std;

int main()
{
    int n;

    cin >> n;

    for (int i = 1; i <= n; i++)
    {
        int temp = i;
        int j = i;
        while (j > 0)
        {
            temp += (j % 10);
            j /= 10;
        }
        if (temp == n) 
        {
            cout << i << endl;
            return 0;
        }
    }
    
    cout << 0 << endl;
    return 0;
}