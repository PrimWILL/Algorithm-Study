#include <stdio.h>

int prob2441(void) {
	int n;
	scanf("%d", &n);

	int len = n;
	while (n--) {
		int cnt = n + 1;
		int cnt_space = len - cnt;
		while (cnt_space--)
			printf(" ");
		while (cnt--)
			printf("*");
		printf("\n");
	}
	return 0;
}