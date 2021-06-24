#include <stdio.h>

int n, s;
int ans = 0;
int ability[22];

void solve(int cur, int sum)
{
	if (cur == n - 1) {
		ans += (sum == s);
		return;
	}
	solve(cur + 1, sum);
	solve(cur + 1, sum + ability[cur + 1]);
}

int main() {
	scanf("%d %d", &n, &s);
	for (int i = 0; i < n; i++)
		scanf("%d", &ability[i]);
	
	solve(0, ability[0]);
	printf("%d\n", ans);
	
	return 0;
}
