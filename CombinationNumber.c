#define _CRT_SECURE_NO_WARNINGS 1

#include<stdio.h>
#include<windows.h>

int main()
{
	int i = 0, j = 0, k = 0;
	int count = 0;
	int m = 0;
	printf("1,2,3,4���ĸ����ֿ�����ɵĻ�����ͬ�Ҳ��ظ����ֵ���λ���ֱ��ǣ�\n");
	for (i = 1; i <= 4; i++)
	{
		for (j = 1; j <= 4; j++)
		{
			if (i == j)                     //ȥ���ظ�����
				continue;
			for (k = 1; k <= 4; k++)
			{
				if ((j == k) || (i == k)) //ȥ���ظ�����
					continue;
				printf("%d%d%d ",i,j,k);
				m++;
				count++;
				if (0 == (count % 10))
					printf("\n");         //ʮ�����ֻ���
					
			}
		}
	}
	printf("\n%d\n",m);
	system("pause");
	return 0;
}