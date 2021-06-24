/*#include <iostream>
using namespace std;

int matrix[110];

int main() 
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> matrix[i];
    
    int maxSum = 0;
    
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                int sum = matrix[i] + matrix[j] + matrix[k];
                if (sum > maxSum && sum <= m) {
                    maxSum = sum;
                }
            }
        }
    }
    cout << maxSum << endl;
    return 0;
}*/

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    int* matrix = new int[n];

    for (int i = 0; i < n; i++)
        cin >> matrix[i];

    int maxSum = 0;
    do {
        int sum = matrix[0] + matrix[1] + matrix[2];
        if (sum > maxSum && sum <= m)
            maxSum = sum;
    } while(next_permutation(matrix, matrix + n));

    cout << maxSum << endl;
    delete[] matrix;
    return 0;
}