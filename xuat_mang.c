#include<stdio.h>
int main()
{
	int row,col,i,j;
	int a[100][100];
	scanf("%d %d",&row, &col);
	for(i=0; i<row; i++)
		for(j=0; j<col; j++)
			scanf("%d", &a[i][j]);
	for(i=0; i<row; i++)
	{
		for(j=0; j<col; j++)
			printf("%3d", a[i][j]);
		printf("\n");
	}
		
}
