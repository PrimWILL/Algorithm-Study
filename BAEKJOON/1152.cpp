#include <stdio.h>

int prob1152(void)
{
	char arr[1000000];
	scanf("%[^\n]s", arr);

	int cnt = 0;
	int k = 0;
	for (int i = 0; arr[i] != NULL; i++)
	{
		if (arr[i] == 32)
			cnt++;
		k = i;
	}
	if (arr[0] == 32 && arr[k] == 32) {
		printf("%d", cnt - 1);
	}
	else if (arr[0] == 32 || arr[k] == 32)
	{
		printf("%d", cnt);
	}
	else
	{
		printf("%d", cnt + 1);
	}
	return 0;
}