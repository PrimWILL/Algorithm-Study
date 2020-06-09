#include <stdio.h>

int prob2438(void) {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		for (int k = 1; k <= i; k++)
			printf("*");
		printf("\n");
	}
	return 0;
}