#include <stdio.h>

int prob10951(void) {
	int a, b;

	while (scanf("%d %d", &a, &b) != EOF)
		printf("%d\n", a + b);
	return 0;
}