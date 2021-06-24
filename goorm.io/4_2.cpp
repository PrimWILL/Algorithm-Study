#include <iostream>
#include <vector>
using namespace std;

bool num[1010000] = { 1, 1 };
vector<int> prime;

int main() {
	for (int i = 2; i * i < 1010000; i++) {
		if (num[i]) continue;
		for (int j = i * i; j < 1010000; j += i) {
			num[j] = 1;
		}
	}
	
	for (int i = 2; i <= 1000000; i++) {
		if (!num[i]) 
			prime.push_back(i);
	}
	
	int n; cin >> n;
	for (int i = 0; i < n; i++) {
		int inputNum;
		cin >> inputNum;
		
		int l = 0, r = prime.size() - 1;
		int prime1 = 0, prime2 = 0;
		
		while(l <= r) {
			int sum = prime[l] + prime[r];
			if (sum == inputNum) {
				prime1 = prime[l];
				prime2 = prime[r];
				l++; r--;
			}
			else if (sum < inputNum) 
				l++;
			else
				r--;
		}
		
		cout << prime1 << ' ' << prime2 << '\n';
	}
	
	return 0;
}