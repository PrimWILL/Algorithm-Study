#include <iostream>
using namespace std;

int box[10001];

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n; 
    cin >> n;

    int temp = 0;   
    for (int i = 0; i < n; i++) {
        cin >> temp;
        box[temp]++;
    }

    for (int i = 1; i <= 10000; i++) {
        while (box[i]) {
            cout << i << '\n';
            box[i]--;
        }
    }
    return 0;
}