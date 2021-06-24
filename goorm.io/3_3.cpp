#include <iostream>
#include <algorithm>
using namespace std;

typedef struct workTime {
	int start;
	int end;
};

bool cmp(const workTime &p1, const  workTime &p2)
{
	if (p1.start < p2.start)
		return true;
	else if (p1.start == p2.start)
		return p1.end < p2.end;
	else
		return false;
}

workTime work[1000010];

int main() {
	int n; cin >> n;
	for (int i = 0; i < n; i++)
		cin >> work[i].start >> work[i].end;
	
	int current = 0;
	int ans = 0;
	int choice = 0;
	
	sort(work, work + n, cmp);
	while (1) {
		if (choice >= n)
			break;
		int minTime = 0;
        int tempstart = 0;
		for (; work[choice].start == current; choice++) {
			if (minTime > work[choice].end)
                tempstart = work[choice].start;
				minTime = work[choice].end;
		}
		current = tempstart;
		ans += 1;
	}
	
	cout << ans << endl;
	return 0;
}