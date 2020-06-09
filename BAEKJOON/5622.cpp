#include <stdio.h>

int prob5622(void) {
	char arr[15];
	scanf("%s", arr);

	int cnt = 0;

	for (int i = 0; arr[i] != NULL; i++)
	{
		if (arr[i] >= 'A' && arr[i] <= 'C')
			cnt += 3;
		else if (arr[i] >= 'D' && arr[i] <= 'F')
			cnt += 4;
		else if (arr[i] >= 'G' && arr[i] <= 'I')
			cnt += 5;
		else if (arr[i] >= 'J'&&arr[i] <= 'L')
			cnt += 6;
		else if (arr[i] >= 'M'&&arr[i] <= 'O')
			cnt += 7;
		else if (arr[i] >= 'P'&&arr[i] <= 'S')
			cnt += 8;
		else if (arr[i] >= 'T'&&arr[i] <= 'V')
			cnt += 9;
		else
			cnt += 10;
	}
	printf("%d", cnt);
	return 0;
}