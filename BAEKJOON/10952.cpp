#include <stdio.h>

int prob10952(void) {
	int a, b;
	
	int flag = 1;
	while (flag) {
		scanf("%d %d", &a, &b);
		if (a == 0 && b == 0) {
			flag = 0;
			break;
		}
		else {
			printf("%d\n", a + b);
		}
	}
	return 0;
}