#include <stdio.h>

int prob1712(void) {
	int a = 0; int b = 0; int c = 0;

	scanf("%d %d %d", &a, &b, &c);
	int k = a / (c - b);
	if (b >= c)
	{
		printf("-1");
	}
	else
	{
		printf("%d", k + 1);
	}
	return 0;
}