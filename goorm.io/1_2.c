#include <stdio.h>

int main() {
	long long int a;
	scanf("%lld", &a);
	
	int ans = 0;
	while(1) {
		if (a == 1) break;
		if (a % 2 == 1) {
			ans = 1;
			break;
		}
		else {
			a = a / 2;
			if (a == 0) break;
		}
	}
	
	if (!ans) printf("Yes\n");
	else printf("No\n");
	
	return 0;
}
