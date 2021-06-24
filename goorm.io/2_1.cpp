#include <iostream>
using namespace std;

typedef long long ll;
typedef struct pos {
	int x;
	int y;
};

ll distance(ll x1, ll x2, ll y1, ll y2)
{
	return ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int main() {
	int n;
	int first = 0, second = 0;
	ll maxDistance = 0;
	
	cin >> n; 
	pos* position = (pos*)malloc(sizeof(pos) * n);
	for (int i = 0; i < n; i++)
		cin >> position[i].x >> position[i].y;
	
	
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			ll positionDistance = distance((ll)position[i].x, (ll)position[j].x, (ll)position[i].y, (ll)position[j].y);
			if (positionDistance > maxDistance) {
				first = i;
				second = j;
				maxDistance = positionDistance;
			}
		}
	}

	cout << first + 1 << ' ' << second + 1;
	
	return 0;
}