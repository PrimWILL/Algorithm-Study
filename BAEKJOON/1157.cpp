#include <stdio.h>

int prob1157(void) {
	char arr[1000000];
	scanf("%s", arr);
	int alpha[26] = { 0 };

	for (int i = 0; i < 26; i++) {
		for (int j = 0; arr[j] != NULL; j++) {
			if (arr[j] == (i + 'a') || arr[j] == (i + 'A'))
			{
				alpha[i]++;
			}
		}
	}

	int maximum = 0;
	int num = 0;
	int cnt = 0;

	for (int k = 0; k < 26; k++)
	{
		if (alpha[k] > maximum) {
			maximum = alpha[k];
			cnt = k;
			num = 0;
		}
		else if (maximum == alpha[k])
		{
			num++;
		}
	}

	if (num > 0) {
		printf("?");
	}
	else
	{
		printf("%c", cnt + 'A');
	}
	return 0;
}