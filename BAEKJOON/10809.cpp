#include <stdio.h>
#include <string.h>

int prob10809(void) {
	char alpha[100];
	scanf("%s", alpha);

	int location[26]; 
	memset(location, -1, sizeof(location)); //location�� �� �迭�� -1�� �ʱ�ȭ

	for (int i = 0; i < 26; i++) {
		for (int j = 0; alpha[j] != NULL; j++) {
			char a = (char)i + 'a';
			if (alpha[j] == a) {
				location[i] = j;
				break;
			}
		}
	}
	for (int k = 0; k < 26; k++)
	{
		printf("%d ", location[k]);
	}
	return 0;
}