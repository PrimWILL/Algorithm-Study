#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> first;
    vector<int> second;
    char input_num = 0;

    string s1, s2;

    cin >> s1 >> s2;

    if (s1.size() < s2.size()) {
        string temp = s2;
        s2 = s1;
        s1 = temp;
    }

    for (int i = 0; i < s1.size(); i++)
        first.push_back(s1[i] - '0');

    for (int i = 0; i < s2.size(); i++)
        second.push_back(s2[i] - '0');

    int first_count = first.size() - 1;
    int second_count = second.size() - 1;

    vector<int> result;
    int carry = 0;

    for (; first_count >= 0; first_count--, second_count--) {
        if (second_count >= 0) {
            int temp = first[first_count] + second[second_count] + carry;
            if (temp > 9) {
                // sum is bigger than 9
                result.push_back(temp % 10);
                carry = 1;
            }
            else {
                // sum is smaller than 10
                result.push_back(temp);
                carry = 0;
            }
        }
        else {
            int temp = first[first_count] + carry;
            if (temp > 9) {
                // sum is bigger than 9
                result.push_back(temp % 10);
                carry = 1;
            }
            else {
                // sum is smaller than 10
                result.push_back(temp);
                carry = 0;
            }
        }
    }

    if (carry)
        result.push_back(carry);

    for(int i = result.size() - 1; i >= 0; i--){
        cout << result[i];
    }
    return 0;
}