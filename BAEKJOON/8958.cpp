#include <stdio.h>

int prob8958(void) {
	int n;
	scanf("%d", &n);

	while (n--) {
		char ox[81];
		scanf("%s", ox);
		int cnt = 0;
		int score = 0;
		for (int j = 0; ox[j] != '\0'; j++) {
			if (ox[j] == 'O') {
				cnt++;
				score = score + cnt;
			}
			else if (ox[j] == 'X')
				cnt = 0;
		}
		printf("%d\n", score);
	}
	return 0;
}