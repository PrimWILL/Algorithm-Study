#include <stdio.h>

int prob1330(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	if (a - b < 0) {
		printf("<\n");
	}
	else if (a - b > 0)
		printf(">\n");
	else
		printf("==");
	return 0;
}