#include <stdio.h>

int prob1924(void) {
	int x, y;
	int res = 0;
	scanf("%d %d", &x, &y);
	if (x == 1) {
		res = (y - 1) % 7;
	}
	else if (x == 2) {
		res = (31 + y - 1) % 7;
	}
	else if (x == 3 || x == 5 || x == 7) {
		res = (28 + 31 * (x / 2) + (x / 2 - 1) * 30 + y - 1) % 7;
	}
	else if (x == 4 || x == 6 || x == 8) {
		res = (28 + 31 * (x / 2) + 30 * (x / 2 - 2) + y - 1) % 7;
	}
	else if (x == 9 || x == 11) {
		res = (28 + 31 * (x / 2 + 1) + (x / 2 - 2) * 30 + y - 1) % 7;
	}
	else {
		res = (28 + 31 * (x / 2) + (x / 2 - 2) * 30 + y - 1) % 7;
	}

	if (res == 1) printf("TUE");
	else if (res == 2) printf("WED");
	else if (res == 3) printf("THU");
	else if (res == 4) printf("FRI");
	else if (res == 5) printf("SAT");
	else if (res == 6) printf("SUN");
	else printf("MON");
	return 0;
}