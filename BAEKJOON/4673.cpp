#include <stdio.h>

int prob4673(void) {
	int num[10000] = { 0 };
	
	/*int t = 1;
	while (t <= 10000) {
		if (num[t] == 0) {
			int a = t;
			if (a <= 10000) {
				int temp = a;
				while (temp / 10) {
					temp = temp / 10;
					a = a + temp;
				}
				a = a + temp;
			}
		}
	}*/
	int k = 334;
	printf("%d", k + k / 1000 + k / 100 + k / 10 + k % 10);
	return 0;
}