#include <stdio.h>

int prob2753(void) {
	int a;
	scanf("%d", &a);

	int res = 0;
	res = a % 4;
	if (res == 0) {
		if ((a % 400) == 0)
			printf("1\n");
		else if ((a % 100) == 0)
			printf("0\n");
		else
			printf("1\n");
	}
	else
		printf("0\n");
	return 0;
}