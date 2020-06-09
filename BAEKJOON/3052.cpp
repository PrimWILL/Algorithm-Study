#include <stdio.h>

int prob3052(void) {
	int num[10];
	for (int i = 0; i < 10; i++) {
		scanf("%d", &num[i]);
	} 
	int res[42] = { 0 };
	for (int j = 0; j < 10; j++) {
		res[num[j] % 42]++;
	}
	int cnt = 0;
	for (int k = 0; k < 42; k++) {
		if (res[k] > 0)
			cnt++;
	}
	printf("%d\n", cnt);
	return 0;
}