#include <stdio.h>

int prob1110(void) {
	int n;
	scanf("%d", &n);

	int cnt = 0;
	int temp = n;

	while (1) {
		if (temp < 10) {
			int a = temp * 10;
			temp = (temp % 10) * 10 + (a / 10 + a % 10) % 10;
		}
		else
	        temp = (temp % 10) * 10 + (temp / 10 + temp % 10) % 10;
		cnt++;
		if (temp == n)
			break;
	}
	printf("%d\n", cnt);
	return 0;
}