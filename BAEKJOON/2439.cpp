#include <stdio.h>

int prob2439(void) {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int k = 1; k <= n - i; k++)
			printf(" ");
		for (int t = 1; t <= i; t++)
			printf("*");
		printf(" \n");
	}
	return 0;
}