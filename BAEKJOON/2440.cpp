#include <stdio.h>

int prob2440(void) {
	int n;
	scanf("%d", &n);

	while (n--) {
		int cnt = n + 1;
		while (cnt--)
			printf("*");
		printf("\n");
	}
	return 0;
}