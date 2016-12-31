#define _CRT_SECURE_NO_WARNINGS 1

#include<stdio.h>
#include<windows.h>

int main()
{
	int i = 0, j = 0, k = 0;
	int count = 0;
	int m = 0;
	printf("1,2,3,4这四个数字可以组成的互不相同且不重复数字的三位数分别是：\n");
	for (i = 1; i <= 4; i++)
	{
		for (j = 1; j <= 4; j++)
		{
			if (i == j)                     //去除重复数字
				continue;
			for (k = 1; k <= 4; k++)
			{
				if ((j == k) || (i == k)) //去除重复数字
					continue;
				printf("%d%d%d ",i,j,k);
				m++;
				count++;
				if (0 == (count % 10))
					printf("\n");         //十个数字换行
					
			}
		}
	}
	printf("\n%d\n",m);
	system("pause");
	return 0;
}