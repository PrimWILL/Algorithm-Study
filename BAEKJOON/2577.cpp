#include <stdio.h>

int prob2577(void) {

	int a, b, c;

	scanf("%d", &a);
	scanf("%d", &b);
	scanf("%d", &c);

	long long num = a * b * c;
	int cnt[10] = { 0 };
	int i = 0;

	while (num > 0) {
		i = num % 10;
		cnt[i]++;
		num = num / 10;
	}

	for (int j = 0; j < 10; j++) {
		printf("%d\n", cnt[j]);
	}
	return 0;
}