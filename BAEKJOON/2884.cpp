#include <stdio.h>

int prob2884(void) {
	int a, b;
	scanf("%d %d", &a, &b);

	if (a != 0) {
		if (b >= 45)
			printf("%d %d\n", a, b - 45);
		else
			printf("%d %d\n", a - 1, b + 60 - 45);
	}
	else {
		if (b >= 45)
			printf("%d %d\n", a, b - 45);
		else
			printf("23 %d\n", b + 60 - 45);
	}
	return 0;
}